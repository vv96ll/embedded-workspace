# Project workspace

## Workspace map

| Path | Purpose |
|---|---|
| requirements/ | Requirements, specifications, acceptance criteria |
| hardware/ | Hardware design and component references |
| firmware/ | Firmware projects and repositories |
| software/ | Companion software and independent tools |
| docs/ | Project design, interfaces, analysis and guides |

Optional paths are added when used. Project-specific build commands and dependencies belong with each project. This workspace can contain independent repositories.

## Agent guidance

Read root AGENTS.md for shared rules and firmware/AGENTS.md for firmware work. Agents without hierarchical loading must read both explicitly. Tool-specific entry points reference these sources when supported.

## Key materials and project entries

| Object | Type | Version | Status | Path/source |
|---|---|---|---|---|

No project facts have been confirmed yet. Add verified entries as materials and projects arrive. Component documents belong under hardware/references/; original SDK packages under references/sdk/. Index externally installed SDK paths instead of copying them unnecessarily.

Group revisions by object and document type. Status: current (adopted), pending (received), superseded (replaced). Newer files do not automatically become current. Keep previous versions and use the current baseline for development.
