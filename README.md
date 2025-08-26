# Hot Cold Rain

This repo holds the world bible for **Point** (Ord–Sar–Widiwidi). It’s organized so in-universe artifacts (“diegetic”) can live alongside out-of-universe canon (systems, eras, timeline). 

**Status**: **WIP**

---
Current baseline: **v0.14**
## What’s new in v0.14 (highlights)
- **Day of the Green Skies/Mutation Day/Green day content is mostly in** - see snapshots/special and snapshot/watershed_moments, along with the /biota folder
- **Test map references** - canon/notes/maps/map_reference.yaml
timeline.csv is canon; timeline.txt is mirror
- **Project restructuring ongoing** - yet another one, may Oboe save our souls. It should make things more readable by LLM and save a shred of my sanity too.
- **Script cleaunp ongoing** - un-blackbox them, because sometimes I need a fix and asking LLM to do it is a pain; regex, open your arms, for here I come.

---

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
- `tools/upload_ready/index_pack.md` — Router-Lite + Front-matter Anthology (single uploadable “map + substance”)
- `tools/upload_ready/systems_digest.md` — compact systems listing
- `tools/upload_ready/entities_*_index.md` — people / factions
- `tools/upload_ready/canon/...` — canonical copies of the above (nested)
- `tools/reports/..._YYYY-MM-DD-HHMMSS.*` — link reports & snapshots (timestamped)

---

## Lore starting point:

- **Master Index (hand-curated entry point)**: `canon/00_master_index.md`

---


## Repository layout (LLM-friendly, shallow)
```
canon/             # lore repo. see master_index for details
tools/             # validators, generators, upload pipeline
```
**Shallow rule:** prefer one level of nesting (two at most for subtypes like Beats houses). Use evocative names; keep indices (index.md, 00_master_index.md) discoverable.

## Two indices, two purposes

  **canon/00_master_index.md** — human-curated landing page (eras, entities, systems, timeline/tools), general "lay of the land"

  **canon/systems/systems_digest.md** (auto) — human-readable inventory of canon docs

---


## Conventions
**Conventions** (IDs, filenames, folders, timeline CSV rules) live in `canon/02_style_guide.md`

---

## Snapshot artifacts (for search & cross-refs)

  **front_matter_anthology.md**(auto)  — flattened front-matter for quick grep across diegetic/notes; includes links to core cosmos/planetology pages. 

  **tools/id_to_path.csv** (auto) — ID → file path map (entities, etc.). Used by other scripts.

  **tools/link_targets.tsv** (auto) — all link targets seen across the tree. Used by other scripts.


---

# Scripts (Git Bash / WSL)

## Build & validation

- **Make snapshots:** tools/make_snapshot.sh → anthology / id map / link targets.
- **Systems listing (human scan, old)**: tools/generate_systems_index.sh → canon/_systems_index.md.
- **Router-Lite (heat map)**: tools/router_lite.py → tools/router_index.md.
- **Link validation: tools/validate_links.py** → tools/link_report.tsv (+ optional link_targets.tsv).
- **Filter report: tools/filter_link_report.py** → tools/link_errors.tsv, tools/link_summary.md.
- **Finalize: tools/finalize_artifacts.sh** files everything into tools/upload_ready/ and tools/reports/.

- **All-in-one (because I'm lazy)**: tools/upload_ready.sh (calls all of the above).

- **timeline.csv validation**: tools/validate_timeline.sh

---
