--- 
id: INDEX:MASTER
name: Master Index — Alt. History Project
status: Stable
updated: 2025-08-25
---

# Welcome / Start here

This is a working map for the canon and tools. Use the **Index Pack** for LLM uploads, the **Systems Digest** (auto, human-centered) for “how it works”, and the **Entity Indices** (auto, human-centered) for quick lookups.

---

## Shortcuts

- **Router (heatmap)**: `tools/router_index.md` (or in Index Pack - Top N by inbound refs; “what’s hot”)
- **Front-matter Anthology (auto)**: `front_matter_anthology.md` (flattened front matter with ids/links/tags)
- **Systems Digest**: `canon/systems/systems_digest.md` (auto, but human-oriented)
- **Glossary**: `01_glossary.md`  •  **Style guide**: `02_style_guide.md`  •  **Map Reference**: `canon/notes/maps/map_reference.yaml`
- **Current GPT prompt**: see the end of `02_style_guide.md`

## Canon structure
- `canon/eras/` (the biggest picture, in dynamic, mainly to show historical vectors, not just at the moment in time)
- `canon/timeline/point_timeline.csv` (timeline with historical events)
- `canon/notes/snapshots` (broad, world-state overviews at a FIXED point in time)
- `canon/entities/` (important historical figures/factions/flora/fauna)
- `canon/systems/{pillar}/` (building blocks for era/snapshots, contains mechanics, institutions, standards, law, tech workings, etc — stable through time or versioned by period)
- `canon/current/goalpost` (the initial outline of “where we are headed”)
- `canon/current/final` (the final outline, based the whole project, the last step)

---

## Upload set (Core files always in repo)
1. `tools/index_pack.md` (Router-Lite + Anthology; regen after big edits)
2. `01_glossary.md` and `02_style_guide.md`
3. `canon/notes/maps/map_reference.yaml`
4. `README.md`
5. Additional context files as required for current editing session.


## Build pipeline

Run the end-to-end pack builder:
```bash
VALIDATE_NO_CASE=1 CLEANUP_MOVE=1 bash tools/upload_ready.sh
```
Outputs land in tools/upload_ready/ and reports in tools/reports/.

---

## Canon stance & "endpoint north star"

  - **Modern baseline** (c. 1803 AO): ~1980s consumer tech aesthetics under unstable supply (patchwork radioshack vibe).
  
  - **Aviation:** rare, expensive, maintenance-heavy; carriers are prestige relics.
  
  - **Space program:** one post-war “peace program” launch; the probe failed → a few iconic images, scandal, cancellation.
  
  - **Media:** radio strong; color TV present but uneven; printing never “lost.”
  
  - **Religio-civic weave:** Good Old Rhythm (Synod & Houses) entwined with Council/courts; calendars, festivals, and convoy law are the social OS.