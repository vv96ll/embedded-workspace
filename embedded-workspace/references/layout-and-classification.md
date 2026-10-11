# Layout and classification

Core directories: `requirements/` (specifications, acceptance criteria, customer clarifications), `hardware/` (schematics, PCB, BOM, wiring), `firmware/` (firmware projects), `software/` (companion applications and independent tools), `docs/` (project-authored architecture, interfaces, analysis, and user guides).

Optional directories:

| Directory | Purpose |
|---|---|
| mechanical/ | CAD, enclosures, assembly |
| assets/ | Shared design assets, graphics, fonts, animation, audio |
| references/ | External reference solutions, unintegrated example code, original SDK packages |
| tasks/ | Plans, issues, progress, relevant lessons |
| tests/ | System tests, hardware integration, measurements and evidence |
| scripts/ | Workspace-level automation |
| releases/ | Versioned deliveries, release notes and manifests |

Keep module-specific assets, unit tests, dependencies, scripts, and build output inside their existing project. A workspace may contain multiple independent repositories; it need not itself be a repository.

## References

- Component datasheets, reference manuals, errata, and application notes: `hardware/references/<vendor-or-component>/`.
- Original vendor SDK packages and accompanying tools: `references/sdk/<vendor>/<name-and-version>/`.
- SDKs and libraries actually used by a build: keep in the owning project's existing dependency structure. Installed external SDKs need an indexed absolute path, not a forced copy.
- External protocol standards: `references/`; the project's own protocol specification: `docs/`.
- Customer materials: classify by purpose rather than putting everything in a customer bucket.
- Keep original filenames and originals. Extracted text or analysis does not replace source documents. Record unknown versions as unconfirmed.

## Index

README contains a workspace map and a key-material table with object, type, version/status, path/source. Use relative links for internal files and explicit paths for external installations. Add provenance URLs when known. Index key manuals, SDK packages, requirements baselines, and project entry points, not every asset. For a large index, use `docs/materials-index.md` and link it from README.

## Ambiguity

A PDF can be a requirement, schematic, datasheet, or guide. A binary can be test input or a delivery. Read enough context to decide. Unknown archives stay in place. Same-name files are never overwritten, even if identical; report duplicates instead of deleting. Root scripts and configuration are not loose materials simply because they are files.
