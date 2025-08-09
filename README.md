# Hot Cold Rain — Canon Workspace

This repo holds the world bible for **Point** (Ord–Sar–Widiwidi). It’s organized so in-universe artifacts (“diegetic”) can live alongside out-of-universe canon (systems, eras, timeline). Currently WIP.

---

## Folder map (what goes where)
canon/
├─ 00_master_index.md # Top-level links into the canon
├─ 01_glossary.md # Terms readers/players will see
├─ 02_style_guide.md # Voice, spelling, AO/BO rules (incl. addendum)
├─ 03_outline_tracker.md # Milestones & “what’s next”
│
├─ timeline/
│ └─ point_timeline.csv # Single source of truth for dated beats (AO can be negative)
│
├─ eras/
│ └─ 00_preord_krum.md # ERA-010 scaffold (Cuzhar Krum thalassocracy)
│ … # Future: ERA-020 “Moss Cities”, ERA-030 “First Blindness”, ERA-100 “Early Ord–Sar”, etc.
│
├─ systems/ # Out-of-universe reference (mechanics, standards)
│ ├─ cosmos/
│ │ ├─ index.md # COS:INDEX-001 — body table + IDs
│ │ ├─ overview.md # COS:SYS-001 — system overview
│ │ ├─ oboe.md # COS:OBE-001 — star
│ │ ├─ moon_hex.md # COS:HEX-001 — Hex (moon)
│ │ ├─ karodot.md # COS:KAR-001 — gas giant
│ │ ├─ bean.md # COS:BEA-001 — inner dwarf
│ │ ├─ ze.md # COS:ZE-001 — outer dwarf
│ │ └─ belts.md # COS:BEL-001 — Karodot’s Tears / Trailing Belt
│ ├─ planetology/
│ │ ├─ point.md # GEO:SYS-001 — tilt, seasons, circulation
│ │ ├─ hydrology.md # GEO:WAT-001 — tides, “green rain”
│ │ └─ geology.md # GEO:TEK-001 — plates, ranges, hazards
│ ├─ tech/
│ │ ├─ arms_armor.md # TECH:ARM-000 — climate/sea-aware kits
│ │ └─ clothing_and_textiles.md# TECH:CLO-000 — materials & dress by era
│ ├─ economy/
│ │ └─ currency_finance.md # ECON:CUR-001 — lira, scrip, insurance
│ ├─ transport/
│ │ └─ index.md # TRANS:IDX-001 — sea, cable/funicular, rail, road
│ ├─ governance/
│ │ └─ law_admin.md # GOV:LAW-001 — Captains → Diet, courts, policing
│ ├─ health/
│ │ └─ public_health.md # HEALTH:PUB-001 — water, clinics, advisories
│ ├─ security/
│ │ └─ piracy_navies.md # SEC:NAV-001 — convoys, letters of marque
│ ├─ metrology_calendar.md # MET:CAL-001 — base-6 habits, 370-day year
│ ├─ agriculture_diet.md # AGRO:DIET-001 — crops, aquaculture, staples
│ └─ language/
│ └─ linguistic_guide.md # LING:SYS-001 — names, morphology, registers
│
├─ entities/
│ ├─ regions/
│ │ └─ bright_sea.yaml # REG:BRI-001 — Bright Sea
│ └─ places/
│ └─ krum_primary_site.yaml # LOC:KRM-001 — Ish-Atu ziggurat complex
│ … (future: people/, orgs/, vessels/, etc.)
│
├─ notes/
│ ├─ diegetic/ # In-universe artifacts (pamphlets, transcripts, etc.)
│ │ ├─ pamphlet_cuzhar_krum.md # Header links to ERA-010 + LOC/REG/COS/GEO
│ │ └─ doc_battle_of_mistakes.md# Documentary script (ERA-100)
│ └─ scratchpad/ # Drafts, TODOs, parking lot
│
└─ art_refs/
└─ map_spec.md # Export variants & helper layers for maps


---

## IDs & cross-refs (cheat sheet)

- **Date system:** `AO` (After Ord City). **Pre-Ord** dates are **negative AO** (e.g., −975 AO). In prose you can say “975 BO”.
- **Event codes:** `EVT-####BO-TAG` for pre-Ord; AO events use positive year. All beats live in `timeline/point_timeline.csv`.
- **IDs (prefix → meaning):**
  - `COS:` cosmos (bodies, belts) — e.g., `COS:HEX-001`
  - `GEO:` planetology/geology — e.g., `GEO:WAT-001`
  - `TECH:` tech (arms/clothing) — e.g., `TECH:ARM-000`
  - `ECON:/TRANS:/GOV:/HEALTH:/SEC:/MET:/AGRO:/LING:` systems
  - `REG:` regions, `LOC:` places, `FAC:` institutions, `PER:` people (when added)

---

## Diegetic header (paste this at top of any in-universe file)

```yaml
---
fact_box:
  title: ""
  doc_type: pamphlet   # pamphlet | transcript | schoolbook | poster | letter | hymn | law | logbook | newspaper | foreword | whatever
  author_in_universe: ""
  date_ao: 0           # integer (negative allowed); null if unknown
  era: ERA-010         # or ERA-100, ERA-700, etc.
  relates_to: [LOC:KRM-001, REG:BRI-001, COS:HEX-001]  # at least one ID; add more as needed
  location_ids: []
  audience: public     # public | elite | military | temple | children
  reliability: medium  # low | medium | high
  source_tier: primary # primary | secondary | reconstruction
  claims:
    - ""
  contradictions: []
  canonical_links:
    - systems/cosmos/index.md

---

Workflow in 60 seconds

    Add beats to timeline/point_timeline.csv (AO can be negative).

    Canon refs live in systems/, eras/, entities/.

    In-universe pieces go in notes/diegetic/ with the YAML header.

    Cross-link with IDs (e.g., COS:HEX-001, GEO:WAT-001, LOC:KRM-001).

    Keep 02_style_guide.md as the arbiter for spelling (e.g., Hex, not Ex).

---

Quick pointers

    Cosmos index: systems/cosmos/index.md (fast way to grab IDs for bodies).

    Planet basics: systems/planetology/point.md (tilt/seasons); hydrology.md (green rain).

    Material culture: systems/tech/… (arms/clothing) with era snapshots.

    Economy/convoys: see economy/currency_finance.md + security/piracy_navies.md.

    Language: systems/language/linguistic_guide.md (names, toponyms, registers).