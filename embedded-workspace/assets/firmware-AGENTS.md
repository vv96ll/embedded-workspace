# Firmware guidance

Apply the workspace AGENTS.md together with these firmware rules. More specific project rules and explicit task requirements take precedence. Agents without hierarchical rule loading must read both files explicitly.

## Project facts
- Before hardware-specific work, locate the exact chip/board, SDK name/version/path, matching examples, toolchain, probe, and existing build/flash commands in the project documentation.
- Record confirmed facts beside the actual project; mark missing facts as unconfirmed. Do not invent commands or hardware parameters.

## Implementation
- Start peripheral work from the closest matching official SDK example or driver. Confirm chip and SDK compatibility.
- Check clock, pin multiplexing, DMA, interrupt priority, startup, and low-power settings against the example and official documentation. Explain meaningful deviations and cite relevant sections for critical changes.
- Examples are starting points; add the error handling actually required by the application.
- Use stdint.h fixed-width types where width matters. Use volatile for hardware registers and appropriate shared accesses; it does not provide atomicity or synchronization.
- Keep interrupt handlers bounded: no blocking, printf, or dynamic allocation. Use the project's existing deferred logging and synchronization mechanisms.
- Avoid dynamic memory unless the project already uses it or the task explicitly requires it.
- Treat warnings in changed code as failures. Use warnings-as-errors where supported without blindly applying it to unchanged vendor code.

## Reusable workflows
- Reuse project build, flash, test, and bounded log-capture scripts. Do not force a new build system or Makefile.
- When asked to establish a programming workflow, complete its first implementation: identify the actual target and probe, choose a supported mature tool, create the reusable command, and run build/program/verification on the available authorized device.
- Use the tool's supported programming verification or readback comparison once; do not repeat equivalent checks after success.
- If hardware or tooling is unavailable, complete the executable script and available checks, report hardware validation as NOT_RUN, and do not call it proven.
- Initialization or file organization alone does not trigger programming. Ordinary erase/program/reset steps within the requested development workflow need no separate questions; irreversible protection/fuse/lock changes do.

## Validation
- Comment-only edits do not need firmware builds. For executable tooling or linked documentation, check only the affected behavior or links.
- For module changes, build and run relevant existing tests; add tests only when they cover meaningful changed behavior or boundaries.
- For clock, interrupts, startup, DMA, and low-power changes, run relevant project checks and identify the device behavior or measurements still needed.
- Stop after relevant checks pass. Investigate new evidence; do not repeatedly run unchanged checks or claim build/program verification proves device functionality.
