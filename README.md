# Hot Cold Rain

This repo holds the world bible for **Point** (Ord–Sar–Widiwidi). It’s organized so in-universe artifacts (“diegetic”) can live alongside out-of-universe canon (systems, eras, timeline). Currently WIP.

---
Current baseline: v0.12

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

## v0.12 highlights

  - Standardized YAML across entities/systems/notes.

  - Timeline CSV hygiene codified + cross-repo validators (Bash & PS).

  - Filled/updated core Ord factions (Council, Synod, Beats 1–6, Censor’s Bench, Keeper, Harbor Watches, Public Debt, Works, Insurance).

  - People canon expanded/found lost in the seas of files (Zambran, Marr, Nerise, Marak; Golden Cadence roll stubs CAD-001…007).

  - Systems cleanup (transport, clothing, cosmos; hydrology/planetology anchors).

  - Diegetic leaf scaffolds (peace circular, pamphlets, extracts, transcripts).