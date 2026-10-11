# AGENTS.md

## Goal and scope
Complete the requested task with the smallest reasonable change. Work autonomously within the requested scope and available permissions.

## Workspace
- Read README.md for directory mappings, project entries, and key references.
- Requirements: requirements/. Hardware and component references: hardware/.
- Firmware: firmware/. Companion software: software/. Project documentation: docs/.
- Follow existing paths and more specific local instructions. Read only relevant context.

## Working style
- Maintain existing code with focused changes and existing patterns.
- For open design tasks, examine requirements and meaningful tradeoffs before implementation. Ask only about decisions that materially affect the result.
- Avoid speculative abstractions, dependencies, unrelated refactoring, and unnecessary process files.
- Report briefly: what changed, what was verified, and what remains unverified.

## Reuse and facts
- Search project implementations and matching official SDK examples first, then suitable maintained open-source components.
- Implement locally when reuse is unsuitable or more costly than simple code.
- Verify dependency compatibility, licensing, and resource needs when selecting components; preserve versions and record relevant decisions.
- Hardware facts come from official documents, matching SDK sources, and project evidence. State uncertainty instead of guessing.

## Execution and validation
- Reuse verified commands and scripts. When a requested recurring workflow lacks an entry point, create and validate a reusable one.
- Execute deterministic sequences together; investigate failures without repeating unchanged attempts.
- Within a requested development-device programming task, perform ordinary programming, verification, and reset without separate confirmations. Ask before irreversible protection, fuse, or locking changes.
- Run the narrowest meaningful validation. Stop after it passes unless inputs change or new evidence warrants further checks.
- Distinguish review, build, software tests, programming verification, device behavior, and physical measurements. Never claim an unperformed check passed.

## Materials and Git
- Organize loose root materials when requested. Preserve originals, projects, repository boundaries, root configuration, and unrelated changes.
- Do not overwrite conflicts or move files with unresolved references. Update indexes and affected links after organization.
- Consult relevant lessons when needed; record reusable corrections concisely in project-local notes when requested or established by the project.
- Initialize structure without automatically importing SDKs, programming devices, or publishing.
- Commit, branch, tag, release, or push only when requested or explicitly required by the active workflow. Do not discard unrelated changes or rewrite shared history.
