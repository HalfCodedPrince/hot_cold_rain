---
id: INDEX:MASTER
name: Master Index (hand-curated entry point)
status: Stable
updated: 2025-08-28
meta:
  style_style: canon/02_style_guide.md
  eiditing_workflow: canon/system_index/editing_workflow.md
  linking_policy: canon/system_index/linking_policy.md
  systems_diachronic_map_core: canon/system_index/systems_diachronic_map_core.md
  systems_diachronic_map_appendix: canon/system_index/systems_diachronic_map_appendix.md
---

# Master Index

# Welcome / Start here

Working map for canon and tools. Use **Index Pack** for LLM uploads, **Systems Digest** for “how it works,” and **Entity Indices** for quick lookups.
---

## Canon structure
- `canon/constants/` — natural or civilizational invariants (link “up” allowed).
- `canon/systems_diachronic/{broad_family}/{pillar}/` — human systems as **era leaves**; pillars are for small subsystems; (`*_cYYYY[-YYYY].md`).
- `canon/snapshots/` — point-in-time overviews; link to same-era leaves and constants.
- `canon/eras/{era_name}/entities/{people,factions}` — people, factions
- `canon/eras/{era_name}` — core bundles of info; main "storyline" leading to /endpoint
- `canon/timeline/point_timeline.csv` — events table. 
- `canon/endpoint/goalpost` — current snippets of what it will look like; currently in flux
- `canon/endpoint/final` — final outline.
---

## Meta docs
- [Style Guide](canon/02_style_guide.md)
- [Editing Workflow](canon/system_index/editing_workflow.md)
- [Linking Policy](canon/system_index/linking_policy.md)
- [Systems Diachronic Map — Core](canon/system_index/systems_diachronic_map_core.md)
- [Systems Diachronic Map — Appendix](canon/system_index/systems_diachronic_map_appendix.md)

---

## Technical limits (editing)
- Header: ≤12 links, ≤350 tokens.
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

## Entry points
- Snapshots: `canon/snapshots/`
- Systems Diachronic: `canon/systems_diachronic/`
- Constants: `canon/constants/`
- Eras: `canon/eras/`

> Note: Meta docs are internal references. Do not link to them from content pages.
