# Agent adapters

The skill's instructions, templates, and Python helper are agent-neutral. Installation and automatic discovery depend on the host tool; consult its current documentation rather than assuming a universal location or syntax.

- Codex: this environment exposes user skills in `~/.codex/skills/<skill-name>/SKILL.md`. Root AGENTS.md is its project guidance entry point. Respect a configured CODEX_HOME or explicitly requested destination.
- Claude Code: when its documented import syntax applies, a root CLAUDE.md containing `@AGENTS.md` shares the same rule source. Do not assume all Claude desktop modes have Claude Code's filesystem capabilities or loading behavior.
- For firmware work under Claude Code, when its import syntax applies, firmware/CLAUDE.md can contain `@../AGENTS.md` and `@AGENTS.md` on separate lines. With another firmware directory, adapt the relative path to the actual workspace root. Other agents must load both guidance files explicitly unless their documented hierarchy handles them.
- Other agents: use their documented project-rule entry point. Prefer an actual supported reference. If only a generated copy is supported, mark it as generated from AGENTS.md and refresh it when the source changes.

Do not create adapters for tools that are not requested or in use. Do not invent import directives. If automatic discovery is unavailable, the user can explicitly provide SKILL.md and the workspace's AGENTS.md as instructions. Rules do not override host permissions.
