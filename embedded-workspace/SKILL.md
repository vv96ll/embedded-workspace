---
name: embedded-workspace
description: Initialize embedded product workspaces, generate shared agent guidance and material indexes, organize root materials, or update this installed skill. Use for workspace setup, file organization, or requests such as "update embedded-workspace", "更新这个 Skill", and "调用 embedded-workspace 更新 Skill".
---

# Embedded Workspace

Manage a product workspace containing requirements, hardware, firmware, companion software, and documentation. These instructions are agent-neutral.

## Scope and discovery

- Select initialize, complete, organize, or update mode from the request. For update mode, go directly to Update this skill; do not initialize or organize the user's workspace. Initialization alone does not include moving existing materials, creating firmware projects, importing SDKs, programming hardware, or committing Git changes.
- Resolve the workspace root; read existing root guidance and README, then inspect immediate entries and relevant subdirectories only.
- Preserve established directory names, projects, repository boundaries, user rules, and unrelated files. Map existing names in README instead of renaming them.
- Read [layout-and-classification.md](references/layout-and-classification.md) for destinations and index conventions. Read [agent-adapters.md](references/agent-adapters.md) when creating an agent entry point or installing this skill.

## Initialize or complete

- For a new product workspace, create requirements, hardware, firmware, software, and docs unless the scope makes one unnecessary. Create optional directories only when needed.
- Run `python <skill-path>/scripts/workspace_ops.py init <workspace-root>` for the default core. It creates root AGENTS.md, firmware/AGENTS.md, README, and ignore rules only if missing. Review and adapt the resulting index to actual facts.
- Firmware-specific rules live in assets/firmware-AGENTS.md and are generated under firmware/. For an existing alternative firmware path, merge the rules there instead of creating a parallel tree. Project facts belong beside the actual engineering project.
- For an existing workspace, prefer targeted additions over the default scaffold when established paths already serve these purposes.
- AGENTS.md is the shared rule source. Preserve existing guidance; merge only relevant compatible additions. Do not guess chip, SDK, probe, command, or version facts.
- Generate only requested or clearly applicable agent entry points. Do not assume every agent automatically reads AGENTS.md or SKILL.md.
- Agents lacking hierarchical rule loading must explicitly read root and firmware guidance when working on firmware; consult the adapter notes for supported imports.
- Add suitable ignore rules while preserving existing ones. Do not ignore formal deliveries or source material indiscriminately.

## Organize root materials

- Organize only when requested. Classify by purpose, using filenames, format, and enough content to decide; extensions alone are insufficient.
- Create destination directories on demand for confidently classified files. Reuse matching existing directories; do not precreate speculative subdivisions or monitor the workspace in the background.
- Move clearly classified loose root files with no unresolved project references. Leave uncertain materials and conflicts in place and report them together.
- Preserve project folders, repositories, packages, and archives as units. Do not automatically unpack archives or move project directories.
- Keep root configuration, guidance, manifests, build files, and entry points in place. Check relevant references before moving files used by projects or scripts.
- Prepare a JSON move plan: `[{"source":"loose-file.pdf","destination":"hardware/references/device/loose-file.pdf"}]` with workspace-relative paths.
- Run `workspace_ops.py move <root> <plan.json> --apply` directly for clear, requested organization. Use preview only when it helps resolve an uncertain batch; do not execute every batch twice.
- The helper rejects escapes, symlinks, protected root files, directories, and existing destinations. It records completed moves under `.workspace-ops/` with hashes. If interrupted, inspect its record and current files before retrying.
- Update README's key-material index and affected document links. No duplicate deletion or automatic conflict replacement.
- Group revisions of the same object and document type together. Track version and adoption status separately: current, pending, or superseded. New arrivals stay pending unless the user or an established project baseline identifies them as current; follow the version rules in layout-and-classification.md.

## Finish

- Trust successful helper output. Check only newly edited index links or reported failures; do not rehash files or rerun initialization after success.
- Restore with `workspace_ops.py restore <root> <record.json> --apply`; use preview only when useful. The helper checks hashes and refuses occupied original paths.
- For guidance-only edits, review the diff; run helper tests only when executable behavior changes. No unrelated builds or hardware tests.
- Report changes, actual validation, and unresolved items concisely. Do not commit, push, or install globally unless requested.

## Update this skill

- Requests such as "更新这个 Skill" or "update embedded-workspace" invoke this mode. The upstream repository is https://github.com/vv96ll/embedded-workspace; use its main branch and install only the embedded-workspace/ folder.
- Locate the active installation and reuse a suitable local checkout, or fetch a temporary checkout. Preserve local edits; when they differ from upstream, use the previous upstream version to identify customizations where available. Merge straightforward compatible changes and report unresolved conflicts rather than overwriting them. If no baseline exists, preserve uncertain differences.
- Synchronize changed skill files, preserving unrelated installation files. Remove obsolete managed files only when their origin and unchanged content are known. Do not update other agents' installations unless requested.
- Leave existing project AGENTS.md files unchanged. Report the installed source commit and update result; stop if already current. Do not commit or push local changes.
- Normal workspace calls use the installed version without checking for updates.
