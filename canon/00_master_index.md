--- 
id: INDEX:MASTER
name: Master Index — Alt. History Project
status: Stable
updated: 2025-08-25
---

# Welcome / Start here

This is the high-level table of contents and working map for the canon and tools. Use the **Index Pack** for LLM uploads, the **Systems Digest** for “how it works”, and the **Entity Indices** for quick lookups.

## Shortcuts

- Router (heatmap): `tools/router_index.md` (or in Index Pack)
- Front-matter Anthology: `front_matter_anthology.md`
- Systems Digest: `canon/systems/systems_digest.md`
- Entities: `canon/entities/people/index.md`, `canon/entities/factions/index.md`, `canon/entities/places/index.md`, `canon/entities/regions/index.md`
- Glossary: `01_glossary.md`  •  Style guide: `02_style_guide.md`  •  Map Digest: `canon/maps/map_digest.md`

## Canon structure
- `canon/eras/` (the biggest picture, in dynamic, mainly to show historical vectors, not just at the moment in time)
- `canon/timeline/point_timeline.csv` (timeline with historical events)
- `canon/notes/snapshots` (broad, world-state overviews at a FIXED point in time)
- `canon/entities/{people,biota,co_types}/` (important historical figures/flora/fauna)
- `canon/systems/{pillar}/` (building blocks for era/snapshots, contains mechanics, institutions, standards, law, tech workings, etc — stable through time or versioned by period)
- `canon/current/goalpost` (the initial outline of “where we are headed”)
- `canon/current/final` (the final outline, based the whole project, the last step)

## Upload set

1. `tools/index_pack.md` (Router-Lite + Anthology)
2. `canon/systems/systems_digest.md`
3. Entities indices (4 files)
4. `01_glossary.md` and `02_style_guide.md`
5. `canon/maps/map_digest.md`
6. 8–10 hot canon pages (by router/topic you're working currently)

## Build pipeline

Run the end-to-end pack builder:
```bash
VALIDATE_NO_CASE=1 CLEANUP_MOVE=1 bash tools/upload_ready.sh
```
Outputs land in tools/upload_ready/ and reports in tools/reports/.