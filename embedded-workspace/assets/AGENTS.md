# AGENTS.md

## Goal and scope
Complete the requested task with the smallest reasonable change. Work autonomously within the requested scope and available permissions.

## Workspace
- Use README.md to locate unfamiliar projects and references; do not reload unchanged context routinely.
- Requirements: requirements/. Hardware and component references: hardware/.
- Firmware: firmware/. Companion software: software/. Project documentation: docs/.
- Follow existing paths and more specific local instructions. Read only relevant context.

## Working style
- Maintain existing code with focused changes and existing patterns.
- For open design tasks, examine requirements and meaningful tradeoffs before implementation. Ask only about decisions that materially affect the result.
- Avoid speculative abstractions, dependencies, unrelated refactoring, and unnecessary process files.
- Make reasonable local decisions and finish the task without step-by-step approval or narration.
- Report briefly: what changed, what was verified, and what remains unverified.

## Reuse and facts
- Search project implementations and matching official SDK examples first, then suitable maintained open-source components.
- Implement locally when reuse is unsuitable or more costly than simple code.
- Check compatibility, licensing, and resource fit when introducing a dependency; reuse established versions without repeating selection work.
- Hardware facts come from official documents, matching SDK sources, and project evidence. State uncertainty instead of guessing.

## Execution and validation
- Reuse working commands and scripts. Create a missing recurring entry point once and run it; trust successful results.
- Execute deterministic sequences together; investigate failures without repeating unchanged attempts.
- Within a requested development-device programming task, perform ordinary programming, verification, and reset without separate confirmations. Ask before irreversible protection, fuse, or locking changes.
- Check only changed behavior. Skip builds for prose-only edits; use existing focused tests for code changes. Do not add tests or audit workflows without a concrete benefit. Stop after success.
- Distinguish review, build, software tests, programming verification, device behavior, and physical measurements. Never claim an unperformed check passed.

## Materials and Git
- Organize loose root materials when requested. Preserve originals, projects, repository boundaries, root configuration, and unrelated changes.
- Preserve conflicting files; check references only when moving executable or linked project files. Update key indexes and affected links.
- Use the indexed current material revision. Group versions by object; keep new arrivals pending until adoption is explicit, retain superseded files, and never choose a baseline from timestamps alone.
- Consult relevant lessons when needed; record reusable corrections concisely in project-local notes when requested or established by the project.
- Initialize structure without automatically importing SDKs, programming devices, or publishing.
- Commit, branch, tag, release, or push only when requested or explicitly required by the active workflow. Do not discard unrelated changes or rewrite shared history.
