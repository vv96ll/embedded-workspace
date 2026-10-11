import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'workspace_ops', BASE / 'embedded-workspace/scripts/workspace_ops.py')
ops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ops)


class WorkspaceOperations(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=BASE)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve() / '\u8d44\u6599 space'
        ops.init(self.root)

    def test_guidance_and_idempotence(self):
        firmware = self.root / 'firmware/AGENTS.md'
        self.assertEqual(firmware.read_bytes(),
                         (BASE / 'embedded-workspace/assets/firmware-AGENTS.md').read_bytes())
        firmware.write_text('custom firmware', encoding='utf-8')
        (self.root / 'AGENTS.md').write_text('custom root', encoding='utf-8')
        ops.init(self.root)
        self.assertEqual(firmware.read_text(), 'custom firmware')
        self.assertEqual((self.root / 'AGENTS.md').read_text(), 'custom root')

    def test_preview_move_and_restore(self):
        original = self.root / 'manual.pdf'
        original.write_bytes(b'reference material')
        plan = [{'source': 'manual.pdf',
                 'destination': 'hardware/references/device/manual.pdf'}]
        moves = ops.checked_moves(self.root, plan)
        ops.execute(self.root, moves, False)
        self.assertTrue(original.exists())
        ops.execute(self.root, moves, True)
        self.assertFalse(original.exists())
        record = json.loads(next((self.root / '.workspace-ops').glob('*.json')).read_text())
        ops.execute(self.root, ops.checked_moves(self.root, record['moves'], True), True)
        self.assertEqual(original.read_bytes(), b'reference material')

    def test_invalid_moves(self):
        (self.root / 'manual.pdf').write_bytes(b'reference')
        for item in [
            {'source': 'manual.pdf', 'destination': '../escape.pdf'},
            {'source': 'manual.pdf', 'destination': 'AGENTS.md'},
            {'source': 'AGENTS.md', 'destination': 'docs/rules.md'},
            {'source': 'firmware', 'destination': 'docs/project'},
        ]:
            with self.subTest(item=item), self.assertRaises(ValueError):
                ops.checked_moves(self.root, [item])

    def test_existing_target_survives(self):
        src, dst = self.root / 'source.pdf', self.root / 'target.pdf'
        src.write_bytes(b'new')
        dst.write_bytes(b'existing')
        with self.assertRaises(FileExistsError):
            ops.move_without_overwrite(src, dst)
        self.assertEqual(dst.read_bytes(), b'existing')
        self.assertEqual(src.read_bytes(), b'new')

    def test_missing_source_cleans_only_new_copy(self):
        dst = self.root / 'new.pdf'
        with self.assertRaises(FileNotFoundError):
            ops.move_without_overwrite(self.root / 'missing.pdf', dst)
        self.assertFalse(dst.exists())

    def test_modified_file_cannot_be_restored(self):
        destination = self.root / 'docs/manual.pdf'
        destination.write_bytes(b'changed')
        item = {'source': 'manual.pdf', 'destination': 'docs/manual.pdf',
                'sha256': 'original-hash'}
        with self.assertRaises(ValueError):
            ops.checked_moves(self.root, [item], restore=True)


if __name__ == '__main__':
    unittest.main()
