# Hot Cold Rain

This repo holds the world bible for **Point** (Ord–Sar–Widiwidi). It’s organized so in-universe artifacts (“diegetic”) can live alongside out-of-universe canon (systems, eras, timeline). Currently WIP.

---
Current baseline: **v0.13**
## What’s new in v0.13 (highlights)
- **Eras:** `07_mangrove_garrot_1200-1290.md`, `08_knotted_lanterns_1290_1400.md`
- **Northlands:** `snapshots/northlands_c0_1400.md`
- **Commerce:** `fog_gate_marts_stern_shore_c0_1400.md`, `mangrove_gardens_c1290_1400.md`, `morum_factors_row_c1296.md`
- **Industry:** `iron_sand_bloomery_c1200.md`, `pozzolan_hydraulic_mortar_c1200.md`, `proto_industry_c1290_1400.md`, `mills_power_wetworld_c1250_1450.md`
- **Learning:** `collegia_and_education_c1310_1400.md`
- **Tech (arms):** `handgonnes_matchlocks_c1300_1500.md`
- **Religion:** `religious_topography_c1290_1400.md` + regional rites (Sar / Knees / Kllrian / Crum)
- **Economy (pre-1300):** `taxation_finance_c0_1200.md` (Ord–Sar)


timeline.csv is canon; timeline.txt is mirror

## Quickstart

```bash
# just clone
git clone <repo>
cd hot_cold_rain
```

- **Master index:** canon/00_master_index.md
- **Style guide:** canon/style_guide.md
- **Glossary:** canon/glossary.md
- **Outline tracker:** canon/outline_tracker.md

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
  eras/                       # period overviews
  entities/
    people/                   # PERS:*
    factions/                 # FAC:* (incl. Beats houses)
    places/                   # LOC:*
    regions/                  # REG:*
    biota/                    # BIO:*
    co_types/                 # CTP:*
  systems/                    # governance, law, economy, tech, cosmos, etc.
  timeline/                   # CSV + tools
  notes/
    diegetic/                 # in-world leafs, transcripts, pamphlets
    rolls/                    # roll lists (e.g., High Masters)
    snapshots/                # concise period/location snapshots
    scratchpad/               # designer notes
tools/                        # validators, scripts
```
**Shallow rule:** prefer one level of nesting (two at most for subtypes like Beats houses). Use evocative names; keep indices (index.md, 00_master_index.md) discoverable.

# Indices & tooling

## Two indices, two purposes

  **canon/00_master_index.md** — curated landing page (eras, entities, systems, timeline/tools). Keep this edited by hand. 

  **canon/_systems_index.md** — auto-generated inventory of system docs; do not hand-edit.

## Snapshot artifacts (for search & cross-refs)

  **front_matter_anthology.md** — flattened front-matter for quick grep across diegetic/notes; includes links to core cosmos/planetology pages. 

  **id_to_path.csv** — ID → file path map (entities, etc.).

  **link_targets.tsv** — all link targets seen across the tree.

  **Conventions** (IDs, filenames, folders, timeline CSV rules) live in 02_style_guide.md

# Scripts (Git Bash / WSL)
**Regenerate the auto index of system docs**
tools/make_systems_index.sh

**Build release snapshots for LLM indexing (front_matter_anthology.md, id_to_path.csv, link_targets.tsv)**
tools/make_snapshot.sh

**Validate the timeline CSV (IDs exist, refs resolve, status flags ok)**
tools/validate_timeline.sh


## Canon stance & “endpoint north star”**

  - Modern baseline (c. 1803 AO): ~1980s consumer tech aesthetics under unstable supply (patchwork radioshack vibe).
  
  - Aviation: rare, expensive, maintenance-heavy; carriers are prestige relics.
  
  - Space program: one post-war “peace program” launch; the probe failed → a few iconic images, scandal, cancellation.
  
  - Media: radio strong; color TV present but uneven; printing never “lost.”
  
  - Religio-civic weave: Good Old Rhythm (Synod & Houses) entwined with Council/courts; calendars, festivals, and convoy law are the social OS.

## v0.13 highlights

- We might be done with the renaming stuff. I swear.
- Files up to the 1200 A.O. added.
- rename_and_fix scripts added for mass renaming and link fixing, if needed (but we are done. Pinky promise)
- validate_timeline is having a fit with the quotes; will fix later 