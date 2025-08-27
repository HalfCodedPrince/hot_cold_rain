---
id: INDEX:MASTER
name: Master Index (hand-curated entry point)
status: Stable
updated: 2025-08-27
meta:
  style: 02_style_guide.md
  workflow: 03_LLM_editing_workflow.md
  linking: 03_LLM_linking_policy.md
---

# Welcome / Start here

Working map for canon and tools. Use **Index Pack** for LLM uploads, **Systems Digest** for “how it works,” and **Entity Indices** for quick lookups.

---

## Canon structure
- `canon/constants/` — natural or civilizational invariants (link “up” allowed).
- `canon/systems_diachronic/{broad_family}/{pillar}/` — human systems as **era leaves**; pillars are for small subsystems; (`*_cYYYY[-YYYY].md`).
- `canon/snapshots/` — point-in-time overviews; link to same-era leaves and constants.
- `canon/entities/{ERA_ID}` — people, factions
- `canon/eras/` — optional bundles or composition pages.
- `canon/timeline/point_timeline.csv` — events table.
- `canon/endpoint/goalpost` — direction of travel.
- `canon/endpoint/final` — final outline.
---

## Meta docs
- Editing workflow: `03_LLM_editing_workflow.md`
- Linking policy: `03_LLM_linking_policy.md`
- Style guide: `02_style_guide.md`

---

## Technical limits (editing)
- Header: ≤12 links, ≤300 tokens.
- File size: warn ≥12 KB, split/trim at 18 KB.
- Keep task file sets small.
- Discovery source of truth: `index_pack.md`. Do not rely on folder indexes.
- Diachronic leaves include a short **Primer**; use `primer_rev` if the primer changes.

---

## Retirement quick reference
- **When:** a new diachronic leaf supersedes scope, or a snapshot becomes the surface for that era.
- **Do:** set `status: Retired` on old leaf; add `links.moved_to: <successor>`; set `derived_from` on successor.
- **Guard:** no new inbound links to Retired (except `derived_from`); move retired files to `/retired/` after one release.

---

## Build pipeline
Run end-to-end pack builder:
```bash
VALIDATE_NO_CASE=1 CLEANUP_MOVE=1 bash tools/upload_ready.sh
