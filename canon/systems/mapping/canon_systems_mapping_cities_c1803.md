---
id: SYS:MAPPING-CITIES-C1803
name: Cities c.1803 — Civic Knobs & Line Mixes (systems dataset)
status: Draft
links:
  inference_rules: canon/systems/mapping/city_inference_rules.md
  map_reference: notes/maps/map_reference.yaml
  map_mutation_day: notes/maps/map_mutation_day.yaml
notes: |
  Timeframe: c.1803 (population tiers from the current burgs CSV). This dataset is also
  used to back-cast 1503–1530 patterns. Ord City historically ~1,000,000 c.1503; 
  present CSV reflects post-war contraction. Religious tags are tentative and currently applied retroactively to 1503.
---

### Field definitions (c.1803 systems dataset)

- **pop_tier (1–5)** — population tier derived from Population (1:<50k, 2:<150k, 3:<300k, 4:<600k, 5:≥600k).
- **biome** — city biome tag from notes/maps.
- **is_port (sea|river|no)** — port type.
- **ward_density (low|med|high)** — built-density proxy from population (use `tower_index` later for finer edits).
- **locks_floodworks (none|some|major)** — scale of hydraulic works at site (derived from port type, biome, precipitation, river_type).
- **beacon_towers (few|many)** — density of signal/beacon towers (from density and large sea ports).
- **sanctuary_grade (A–D)** — quality of Sanctuary infrastructure & protections (A best); used for premiums, clinic access, legal rights.
- **convoy_node_rank (1–5)** — convoy-network centrality (temporary proxy: population quintiles; replace with traffic when available).
- **line_mix {{otter|fox|bat %}}** — relative share of Co-Type lines (derived weights normalized to 100%). Dialects remain street-level “types.”
- **dialects** — ward-visible dialects (e.g., reedcat, quay-bat, longfoot, cold-*).
- **dominant_religion** — most prevalent cult/rite in 1803 (tentative; applied retroactively to 1503 where needed).
- **media_index (low|medium|high)** — mass-media infrastructure (radio/TV/press). High for capitals or large hubs.
- **unrest_baseline (0–5)** — modern unrest propensity baseline (density + media mobilization; dampened by strong sanctuaries, strong insurance co-ops, and ritual outlets such as Lotus/Splendid).

> Removed for clarity in c.1803: **mixed_court_load_per_hexad** (needs better inputs) and **rumor_pressure** (now lives only in the 1503–1530 overlay).


```yaml
cities:
  - name: Tau-Hi
    pop_tier: 5
    biome: temperate_rainforest
    is_port: sea
    ward_density: high
    locks_floodworks: some
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 5
    line_mix: { otter: 45%, fox: 30%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "Good Old Rhythm - Lotus"
    media_index: high
    unrest_baseline: 3
  - name: Haru-ahru
    pop_tier: 5
    biome: wetland
    is_port: sea
    ward_density: high
    locks_floodworks: major
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 5
    line_mix: { otter: 50%, fox: 25%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 4
  - name: Knees
    pop_tier: 5
    biome: tropical_rainforest
    is_port: sea
    ward_density: high
    locks_floodworks: some
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 5
    line_mix: { otter: 45%, fox: 30%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 4
  - name: Kroth
    pop_tier: 5
    biome: tropical_rainforest
    is_port: river; center of the island biggest island
    ward_density: high
    locks_floodworks: major
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 5
    line_mix: { otter: 50%, fox: 25%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 4
  - name: Seven Fingers
    pop_tier: 5
    biome: tropical_rainforest
    is_port: sea
    ward_density: high
    locks_floodworks: some
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 5
    line_mix: { otter: 45%, fox: 30%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "Good Old Rhythm - Lotus"
    media_index: high
    unrest_baseline: 3
  - name: Grakk
    pop_tier: 5
    biome: tropical_rainforest
    is_port: river; lake adjacent
    ward_density: high
    locks_floodworks: major
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 4
    line_mix: { otter: 50%, fox: 25%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 4
  - name: Koi-Hi
    pop_tier: 5
    biome: wetland
    is_port: sea
    ward_density: high
    locks_floodworks: major
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 4
    line_mix: { otter: 50%, fox: 25%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 4
  - name: Morum
    pop_tier: 4
    biome: temperate_rainforest
    is_port: sea
    ward_density: med
    locks_floodworks: major
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 4
    line_mix: { otter: 55%, fox: 25%, bat: 20% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "Good Old Rhythm - Lotus"
    media_index: high
    unrest_baseline: 2
  - name: Ord-Kahet
    pop_tier: 4
    biome: tropical_seasonal_forest
    is_port: sea
    ward_density: med
    locks_floodworks: some
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 4
    line_mix: { otter: 40%, fox: 35%, bat: 25% }
    dialects: [longfoot, quay-bat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 3
  - name: Vitrana
    pop_tier: 4
    biome: tropical_rainforest
    is_port: sea
    ward_density: med
    locks_floodworks: some
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 4
    line_mix: { otter: 45%, fox: 30%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: high
    unrest_baseline: 3
  - name: Gamunka
    pop_tier: 3
    biome: temperate_deciduous_forest
    is_port: river
    ward_density: med
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: B
    convoy_node_rank: 3
    line_mix: { otter: 45%, fox: 20%, bat: 35% }
    dialects: [longfoot, quay-bat]
    dominant_religion: "No religion"
    media_index: medium
    unrest_baseline: 2
  - name: Honor
    pop_tier: 3
    biome: wetland
    is_port: sea
    ward_density: med
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: B
    convoy_node_rank: 3
    line_mix: { otter: 60%, fox: 15%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: medium
    unrest_baseline: 2
  - name: Wur
    pop_tier: 3
    biome: temperate_deciduous_forest
    is_port: sea
    ward_density: med
    locks_floodworks: some
    beacon_towers: many
    sanctuary_grade: B
    convoy_node_rank: 3
    line_mix: { otter: 40%, fox: 20%, bat: 40% }
    dialects: [longfoot, quay-bat]
    dominant_religion: "Good Old Rhythm"
    media_index: medium
    unrest_baseline: 2
  - name: Fo
    pop_tier: 3
    biome: temperate_rainforest
    is_port: river
    ward_density: med
    locks_floodworks: major
    beacon_towers: few
    sanctuary_grade: B
    convoy_node_rank: 3
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "No religion"
    media_index: medium
    unrest_baseline: 2
  - name: Yafa
    pop_tier: 3
    biome: temperate_rainforest
    is_port: river
    ward_density: med
    locks_floodworks: major
    beacon_towers: few
    sanctuary_grade: B
    convoy_node_rank: 3
    line_mix: { otter: 60%, fox: 15%, bat: 25% }
    dialects: [longfoot, quay-bat, reedcat]
    dominant_religion: "Good Old Rhythm"
    media_index: medium
    unrest_baseline: 2
  - name: Moss City
    pop_tier: 2
    biome: temperate_deciduous_forest
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 2
    line_mix: { otter: 60%, fox: 20%, bat: 20% }
    dialects: [cold-fox, cold-otter, longfoot]
    dominant_religion: "No religion"
    media_index: medium
    unrest_baseline: 1
  - name: Ord City
    pop_tier: 2
    biome: temperate_rainforest
    is_port: river
    ward_density: low
    locks_floodworks: major
    beacon_towers: many
    sanctuary_grade: C
    convoy_node_rank: 2
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot, reedcat]
    dominant_religion: "Good Old Rhythm"
    media_index: medium
    unrest_baseline: 1
  - name: New Roots
    pop_tier: 2
    biome: wetland
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 2
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot, reedcat]
    dominant_religion: "No religion"
    media_index: medium
    unrest_baseline: 1
  - name: Camu-Se
    pop_tier: 2
    biome: wetland
    is_port: river
    ward_density: low
    locks_floodworks: major
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 2
    line_mix: { otter: 70%, fox: 15%, bat: 15% }
    dialects: [longfoot, reedcat]
    dominant_religion: "No religion"
    media_index: medium
    unrest_baseline: 1
  - name: North-Se
    pop_tier: 1
    biome: taiga
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 2
    line_mix: { otter: 60%, fox: 20%, bat: 20% }
    dialects: [cold-fox, cold-otter, longfoot]
    dominant_religion: "No religion"
    media_index: low
    unrest_baseline: 1
  - name: Black Roots
    pop_tier: 1
    biome: wetland
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 1
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot, reedcat]
    dominant_religion: "No religion"
    media_index: low
    unrest_baseline: 1
  - name: Lake Exchange
    pop_tier: 1
    biome: temperate_deciduous_forest
    is_port: river; lake adjacent
    ward_density: low
    locks_floodworks: major
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 1
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot]
    dominant_religion: "No religion"
    media_index: low
    unrest_baseline: 1
  - name: Tau-Hi Delta Citadel
    pop_tier: 1
    biome: temperate_deciduous_forest
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 1
    line_mix: { otter: 50%, fox: 25%, bat: 25% }
    dialects: [longfoot]
    dominant_religion: "Good Old Rhythm - Lotus"
    media_index: low
    unrest_baseline: 0
  - name: Bo-Dan
    pop_tier: 1
    biome: wetland
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 1
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot, reedcat]
    dominant_religion: "No religion"
    media_index: low
    unrest_baseline: 1
  - name: Lower Ord
    pop_tier: 1
    biome: temperate_rainforest
    is_port: sea
    ward_density: low
    locks_floodworks: some
    beacon_towers: few
    sanctuary_grade: C
    convoy_node_rank: 1
    line_mix: { otter: 65%, fox: 15%, bat: 20% }
    dialects: [longfoot, reedcat]
    dominant_religion: "Good Old Rhythm"
    media_index: low
    unrest_baseline: 1
```
