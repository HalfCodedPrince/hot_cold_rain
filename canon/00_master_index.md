--- 
id: INDEX:MASTER
name: Master Index — Alt. History Project
status: Stable
updated: 2025-08-19
---

# Welcome / Start here

This is the high-level table of contents and working map for the canon and tools. Use the **Index Pack** for LLM uploads, the **Systems Digest** for “how it works”, and the **Entity Indices** for quick lookups.

## Shortcuts

- Router (heatmap): `tools/router_index.md` (or in Index Pack)
- Front-matter Anthology: `front_matter_anthology.md`
- Systems Digest: `canon/systems/systems_digest.md`
- Systems Listing (human scan): `canon/_systems_index.md`
- Entities: `canon/entities/people/index.md`, `canon/entities/factions/index.md`, `canon/entities/places/index.md`, `canon/entities/regions/index.md`
- Glossary: `01_glossary.md`  •  Style guide: `02_style_guide.md`  •  Map Digest: `canon/maps/map_digest.md`

## Canon structure

- `canon/entities/` — People, factions, places, regions, biota
- `canon/systems/` — Governance, economy, tech, transport, health, religion, etc.
- `canon/eras/` — Era overviews and packs
- `canon/maps/` — Map digest and geography notes

## Upload set

1. `tools/index_pack.md` (Router-Lite + Anthology)
2. `canon/systems/systems_digest.md`
3. Entities indices (4 files)
4. `01_glossary.md` and `02_style_guide.md`
5. `canon/maps/map_digest.md`
6. 8–10 hot canon pages (by router)

## Build pipeline

Run the end-to-end pack builder:
```bash
VALIDATE_NO_CASE=1 CLEANUP_MOVE=1 bash tools/upload_ready.sh
```
Outputs land in tools/upload_ready/ and reports in tools/reports/.