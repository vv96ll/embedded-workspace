"""Agent-neutral workspace operations; Python 3.9+, standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import uuid

CORE = ('requirements', 'hardware', 'firmware', 'software', 'docs')
PROTECTED = {'agents.md', 'claude.md', 'readme.md', '.gitignore', '.gitattributes',
             '.gitmodules', 'makefile', 'cmakelists.txt', 'package.json',
             'package-lock.json', 'platformio.ini', 'pyproject.toml'}


def safe(root, relative):
    p = Path(relative)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError(f'Invalid relative path: {relative}')
    candidate = root / p
    for part in [candidate, *candidate.parents]:
        if part == root:
            break
        if part.is_symlink() or (hasattr(part, 'is_junction') and part.is_junction()):
            raise ValueError(f'Link traversal refused: {relative}')
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root) or resolved == root:
        raise ValueError(f'Path escapes workspace: {relative}')
    return candidate


def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def init(root):
    root.mkdir(parents=True, exist_ok=True)
    for name in CORE:
        safe(root, name).mkdir(exist_ok=True)
    assets = Path(__file__).resolve().parents[1] / 'assets'
    for template, name in [('AGENTS.md', 'AGENTS.md'),
                           ('firmware-AGENTS.md', 'firmware/AGENTS.md'),
                           ('workspace-readme.md', 'README.md')]:
        target = safe(root, name)
        if not target.exists():
            with target.open('xb') as f:
                f.write((assets / template).read_bytes())
    ignore = safe(root, '.gitignore')
    if not ignore.exists():
        with ignore.open('x', encoding='utf-8') as f:
            f.write('__pycache__/\n*.py[cod]\n.workspace-ops/\n')
    print(f'Initialized (existing files preserved): {root}')


def checked_moves(root, items, restore=False):
    if not isinstance(items, list):
        raise ValueError('Plan must be a JSON list')
    result, used = [], set()
    for item in items:
        source, destination = item['source'], item['destination']
        if restore:
            source, destination = destination, source
        src, dst = safe(root, source), safe(root, destination)
        if not src.is_file():
            raise ValueError(f'Source is not a regular file: {source}')
        if not restore and (src.parent != root or src.name.lower() in PROTECTED
                            or src.name.startswith('.') or src.suffix.lower() in
                            {'.py', '.ps1', '.bat', '.cmd', '.sh', '.toml', '.yaml', '.yml'}):
            raise ValueError(f'Not an eligible loose root material: {source}')
        if dst.exists() or src == dst:
            raise ValueError(f'Destination exists: {destination}')
        keys = {os.path.normcase(str(src)), os.path.normcase(str(dst))}
        if keys & used:
            raise ValueError('Overlapping paths in move batch')
        used.update(keys)
        checksum = digest(src)
        if restore and checksum != item['sha256']:
            raise ValueError(f'Moved file has changed: {source}')
        result.append((src, dst, checksum))
    return result


def move_without_overwrite(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with dst.open('xb') as output:
            created = True
            with src.open('rb') as incoming:
                shutil.copyfileobj(incoming, output)
    except FileExistsError:
        raise
    except BaseException:
        if created and dst.exists():
            dst.unlink()
        raise
    shutil.copystat(src, dst)
    src.unlink()


def execute(root, moves, apply):
    for src, dst, _ in moves:
        print(f'{src.relative_to(root)} -> {dst.relative_to(root)}')
    if not apply or not moves:
        print('Preview only' if not apply else 'No moves')
        return
    records = safe(root, '.workspace-ops')
    records.mkdir(exist_ok=True)
    record = records / f'moves-{uuid.uuid4().hex}.json'
    data = {'workspace': str(root), 'moves': []}
    record.write_text(json.dumps(data, indent=2), encoding='utf-8')
    for src, dst, checksum in moves:
        entry = {'source': str(src.relative_to(root)),
                 'destination': str(dst.relative_to(root)),
                 'sha256': checksum, 'status': 'pending'}
        data['moves'].append(entry)
        record.write_text(json.dumps(data, indent=2), encoding='utf-8')
        move_without_overwrite(src, dst)
        entry['status'] = 'complete'
        record.write_text(json.dumps(data, indent=2), encoding='utf-8')
    print(f'Record: {record}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['init', 'move', 'restore'])
    parser.add_argument('root', type=Path)
    parser.add_argument('plan', nargs='?', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if args.root.is_symlink() or (hasattr(args.root, 'is_junction') and args.root.is_junction()):
        parser.error('Workspace root must not be a link')
    root = args.root.resolve()
    try:
        if args.operation == 'init':
            init(root)
        else:
            if args.plan is None:
                raise ValueError('A plan or record JSON file is required')
            data = json.loads(args.plan.read_text(encoding='utf-8-sig'))
            restore = args.operation == 'restore'
            if restore:
                if data['workspace'] != str(root):
                    raise ValueError('Record belongs to a different workspace')
                data = [item for item in data['moves'] if item['status'] == 'complete']
            execute(root, checked_moves(root, data, restore), args.apply)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'ERROR: {error}\n')


if __name__ == '__main__':
    main()
