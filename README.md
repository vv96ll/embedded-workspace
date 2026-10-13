# Embedded Workspace Skill

English | [简体中文](README.zh-CN.md)

An agent-neutral skill for initializing embedded product workspaces, organizing loose root materials, generating shared AGENTS.md guidance, and maintaining key-material indexes.

The reusable skill is in [embedded-workspace/SKILL.md](embedded-workspace/SKILL.md). It supports Windows, Linux, and macOS with Python 3.9+ and the standard library. No firmware generator, SDK, or hardware is required.

Initialization generates shared root AGENTS.md and scoped firmware/AGENTS.md. Firmware guidance includes SDK example reuse, ISR constraints, memory/type/warning rules, first-use script validation, and proportional checks. Existing guidance is preserved; agents merge relevant updates during completion tasks. Root materials are organized only on request; destination directories are created as needed.

Copy `embedded-workspace/` into your agent's documented skill location, or explicitly provide SKILL.md to an agent that can access local files. See [agent adapters](embedded-workspace/references/agent-adapters.md); automatic discovery is tool-specific.

```text
python embedded-workspace/scripts/workspace_ops.py init /path/to/workspace
python embedded-workspace/scripts/workspace_ops.py move /path/to/workspace plan.json --apply
python embedded-workspace/scripts/workspace_ops.py restore /path/to/workspace record.json --apply
```

Move plans contain workspace-relative `source` and `destination` fields. The agent determines classification; the helper validates paths, previews changes, refuses overwrites, and records reversible moves. Initialization preserves existing files and does not initialize Git or program hardware.

## Installation

Clone `https://github.com/vv96ll/embedded-workspace.git`. Copy the inner `embedded-workspace/` folder into your agent's documented skill directory, not the entire repository. For default Codex, use `~/.codex/skills/embedded-workspace/` (respect configured CODEX_HOME). For Claude Code, use its documented user or project skill location, such as `~/.claude/skills/embedded-workspace/` or `.claude/skills/embedded-workspace/`. Other agents can read SKILL.md explicitly if skill discovery is unavailable. Start a new session if the catalog does not refresh. Desktop chat apps may not have coding agents' filesystem capabilities.

## Updating an installed skill

Invoke this skill's update mode:

> Use embedded-workspace to update itself.

The skill fetches upstream main and updates the active installation while preserving local edits and existing project AGENTS.md files. Network and installation write access are needed. Normal calls do not check for updates; other installations are updated only when requested. Agents without automatic discovery must first load SKILL.md explicitly.

## Agent requests

- “Use embedded-workspace to initialize this product workspace; do not create firmware projects or move existing materials.”
- “Organize newly added root materials by purpose, and update the material index. Leave uncertain files in place.”
- “Complete guidance and indexes while preserving existing directory names and repositories.”

No background watcher is installed. Core directories are requirements, hardware, firmware, software, and docs. Optional mechanical, assets, references, tasks, tests, scripts, and releases directories are created when needed. Component documents go under hardware/references; original SDK packages under references/sdk. Build dependencies stay with their projects. Agents without hierarchical rule loading must read root and firmware guidance explicitly.

## Move plan and recovery

Use a UTF-8 JSON file with workspace-relative paths:

```json
[{"source":"manual.pdf","destination":"hardware/references/component/manual.pdf"}]
```

Quote paths containing spaces. Use --apply directly for clear requested moves; omit it for an optional preview. Missing destination parents are created automatically. The helper does not classify content or update Markdown indexes; the agent handles those steps. It refuses protected root files, directories, links, path escapes, and existing destinations.

Records with hashes are written under `.workspace-ops/moves-<id>.json`. Pass the printed record path with --apply to restore; preview is optional. Hashes protect restoration against changed files; routine copying does not perform an extra hash comparison. Restore refuses changed files or occupied original paths. Update affected indexes afterward. Following interruption, inspect pending entries and actual paths before retrying.

## Validation

For helper code changes, run `python -m unittest discover -s tests -v`; prose-only changes need a diff review. Trust successful helper output instead of repeating initialization or rehashing files. Development rules favor direct execution, existing scripts, one affected build/test pass, and no speculative tests or mandatory audit process. Current automated execution covers Windows; Linux and macOS have not been tested. Initialization preserves existing files; merging existing rules and alternate layouts is agent-assisted. It does not build, program hardware, initialize Git, commit, or publish. Report unavailable hardware checks as NOT_RUN.
