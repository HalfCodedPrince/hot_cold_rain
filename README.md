# Hot Cold Rain

This repo holds the world bible for **Point** (Ord–Sar–Widiwidi). It’s organized so in-universe artifacts (“diegetic”) can live alongside out-of-universe canon (systems, eras, timeline). Currently WIP.

---
Current baseline: **v0.14**
## What’s new in v0.14 (highlights)
- **Day of the Green Skies/Mutation Day/Green day content is mostly in** - see snapshots/special and snapshot/watershed_moments, along with the /biota folder
- **Test map references** - canon/notes/maps/map_reference.yaml
timeline.csv is canon; timeline.txt is mirror

## Quickstart

```bash
# clone
git clone <repo>
cd hot_cold_rain

# one-command build: snapshots, router, validation, indices, upload pack
# (Windows Git Bash / WSL / macOS)
VALIDATE_NO_CASE=1 CLEANUP_MOVE=1 bash tools/upload_ready.sh
```
**Outputs:**
- tools/upload_ready/index_pack.md — Router-Lite + Front-matter Anthology (single uploadable “map + substance”)
- tools/upload_ready/systems_digest.md — compact systems listing
- tools/upload_ready/entities_*_index.md — people / factions / places / regions
- tools/upload_ready/canon/... — canonical copies of the above (nested)
- tools/reports/..._YYYY-MM-DD-HHMMSS.* — link reports & snapshots (timestamped)

## Where to start

- **Master Index (hand-curated, mostly)**: canon/00_master_index.md
- **Front-matter Anthology (auto)**: front_matter_anthology.md (flattened front matter with ids/links/tags)
- **Router (auto)**: tools/router_index.md (Top N by inbound refs; “what’s hot”)
- **Entity Indices** (auto):
canon/entities/people/index.md, canon/entities/factions/index.md,
canon/entities/places/index.md, canon/entities/regions/index.md
- **Systems Digest (auto)**: canon/systems/systems_digest.md
**Glossary (hand)**: 01_glossary.md
**Style Guide (hand)**: 02_style_guide.md

## File format (all canonical pages)
```
---
id: FAC:COC-001
name: Council of Captains
status: Stable
links:
  governance: canon/systems/governance/empty_seat.md
---
```
**IDs**: PERS:…, FAC:…, LOC:…, REG:…, ERA-*, EVT-*, etc.

**Filenames**: snake_case.md.

**Cross-refs**: store under links: by short keys (no deep links to Drafts from Stable).

## Timeline CSV
- **Path**: canon/timeline/point_timeline.csv
- **Header** must be exactly:
```
ao,code,title,where,who,summary,impact,refs,status
```
- **where / who** use IDs (semicolon-separated, may be quoted).
- **refs** are |-separated repo paths (anchors allowed).
- **status** ∈ {Stable, Draft, Contested}.

## timeline.csv validators:
- **Bash:** ./tools/validate_timeline.sh

## Repository layout (LLM-friendly, shallow)
```
canon/
  00_master_index.md
  entities/        # people, factions, places, regions (+ biota / co_types)
  systems/         # governance, economy, tech, transport, health, religion, etc.
  eras/            # era overviews & packs
  maps/            # map digest & geography notes
  timeline/        # CSV + tools
tools/             # validators, generators, upload pipeline
```
**Shallow rule:** prefer one level of nesting (two at most for subtypes like Beats houses). Use evocative names; keep indices (index.md, 00_master_index.md) discoverable.

# Indices & tooling

## Two indices, two purposes

  **canon/00_master_index.md** — curated landing page (eras, entities, systems, timeline/tools).

  **canon/_systems_index.md** — auto-generated inventory of system docs; do not hand-edit.

## Snapshot artifacts (for search & cross-refs)

  **front_matter_anthology.md** — flattened front-matter for quick grep across diegetic/notes; includes links to core cosmos/planetology pages. 

  **tools/id_to_path.csv** — ID → file path map (entities, etc.).

  **tools/link_targets.tsv** — all link targets seen across the tree.

**Conventions** (IDs, filenames, folders, timeline CSV rules) live in 02_style_guide.md

# Scripts (Git Bash / WSL)
**Regenerate the auto index of system docs**
tools/make_systems_index.sh

## Build & validation

- **Make snapshots:** tools/make_snapshot.sh → anthology / id map / link targets.
- **Systems listing (human scan)**: tools/generate_systems_index.sh → canon/_systems_index.md.
- **Router-Lite (heat map)**: tools/router_lite.py → tools/router_index.md.
- **Link validation: tools/validate_links.py** → tools/link_report.tsv (+ optional link_targets.tsv).
- **Filter report: tools/filter_link_report.py** → tools/link_errors.tsv, tools/link_summary.md.
- **Finalize: tools/finalize_artifacts.sh** files everything into tools/upload_ready/ and tools/reports/.

- **All-in-one (because I'm lazy)**: tools/upload_ready.sh (calls all of the above).

## Canon stance & “endpoint north star”**

  - Modern baseline (c. 1803 AO): ~1980s consumer tech aesthetics under unstable supply (patchwork radioshack vibe).
  
  - Aviation: rare, expensive, maintenance-heavy; carriers are prestige relics.
  
  - Space program: one post-war “peace program” launch; the probe failed → a few iconic images, scandal, cancellation.
  
  - Media: radio strong; color TV present but uneven; printing never “lost.”
  
  - Religio-civic weave: Good Old Rhythm (Synod & Houses) entwined with Council/courts; calendars, festivals, and convoy law are the social OS.