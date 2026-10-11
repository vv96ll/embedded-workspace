---
name: embedded-workspace
description: Initialize embedded product workspaces, generate shared agent guidance and material indexes, and organize loose root materials by purpose. Use for workspace setup, structure completion, or requested root-file organization across AI agents.
---

# Embedded Workspace

Manage a product workspace containing requirements, hardware, firmware, companion software, and documentation. These instructions are agent-neutral.

## Scope and discovery

- Select initialize, complete, or organize mode from the request. Initialization alone does not include moving existing materials, creating firmware projects, importing SDKs, programming hardware, or committing Git changes.
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
- Run `workspace_ops.py move <root> <plan.json>` to preview, then add `--apply` to execute authorized organization. Preview is an internal check, not a mandatory permission question.
- The helper rejects escapes, symlinks, protected root files, directories, and existing destinations. It records completed moves under `.workspace-ops/` with hashes. If interrupted, inspect its record and current files before retrying.
- Update README's key-material index and affected document links. No duplicate deletion or automatic conflict replacement.

## Finish

- Verify created files, index paths, and completed moves. Repeated initialization must preserve existing content.
- For restoration, use `workspace_ops.py restore <root> <record.json>` to preview, then `--apply`. It checks hashes and refuses occupied original paths.
- Run only checks meaningful to these file operations; no unrelated builds or hardware tests.
- Report changes, actual validation, and unresolved items concisely. Do not commit, push, or install globally unless requested.
