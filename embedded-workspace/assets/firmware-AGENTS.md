# Firmware guidance

Apply the workspace AGENTS.md together with these firmware rules. More specific project rules and explicit task requirements take precedence. Agents without hierarchical rule loading must read both files explicitly.

## Project facts
- Reuse documented chip, SDK, toolchain, probe, and commands. Look up missing facts only when needed for the task; do not repeat environment discovery.

## Implementation
- Start peripheral work from the closest matching official SDK example or driver. Confirm chip and SDK compatibility.
- For changed clock, pin, DMA, interrupt, startup, or sleep settings, consult matching examples and documentation. Explain non-obvious deviations; avoid mandatory citations for routine changes.
- Examples are starting points; add the error handling actually required by the application.
- Use stdint.h fixed-width types where width matters. Use volatile for hardware registers and appropriate shared accesses; it does not provide atomicity or synchronization.
- Keep interrupt handlers bounded: no blocking, printf, or dynamic allocation. Use the project's existing deferred logging and synchronization mechanisms.
- Avoid dynamic memory unless the project already uses it or the task explicitly requires it.
- Fix warnings introduced by the change; retain the existing build warning policy.
- Use watchdogs when required; preserve existing behavior. Feed only on verified critical-task progress, with timeouts covering worst-case execution and documented startup, update, and sleep behavior.
- When changing watchdog behavior, check normal operation and stall recovery when hardware is available; otherwise report the gap.

## Reusable workflows
- Reuse project build, flash, test, and bounded log-capture scripts. Do not force a new build system or Makefile.
- When asked to establish a programming workflow, complete its first implementation: identify the actual target and probe, choose a supported mature tool, create the reusable command, and run build/program/verification on the available authorized device.
- Use the tool's built-in programming verification once; read back separately only when built-in verification is unavailable. Continue directly after success.
- If hardware or tooling is unavailable, complete the executable script and available checks, report hardware validation as NOT_RUN, and do not call it proven.
- Initialization or file organization alone does not trigger programming. Ordinary erase/program/reset steps within the requested development workflow need no separate questions; irreversible protection/fuse/lock changes do.

## Validation
- Skip firmware builds for comments and documentation. Check edited commands or links only when relevant.
- For code changes, build once and run affected existing tests. Add a test only for a meaningful regression or boundary; do not expand to full suites by default.
- For hardware-sensitive changes, check the affected behavior on available hardware; identify untested behavior without blocking unrelated progress.
- Stop after relevant checks pass. Investigate new evidence; do not repeatedly run unchanged checks or claim build/program verification proves device functionality.
