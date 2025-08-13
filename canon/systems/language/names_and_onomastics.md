---
id: LING:NAMES-001
name: Names & Onomastics (Ord–Sar)
status: Draft
links:
  suffixes: canon/systems/language/onomastic_suffixes.md
tags: [names, onomastics]
---

# Names & Onomastics (Ord–Sar)

## Why it looks messy 
Ord–Sar is a thalassocracy of layered peoples and paperwork. Multiple naming systems coexist because the **sea** connects faster than the **law** standardizes. In practice, a person carries one **ledger-name** for courts and several **street-names** for life.

---

## The four big patterns (use whichever fits the person)
1) **Patronymic** — “X, son/daughter of Y”
   - Early Ord default; still common in working ports and soldier rolls.
   - Ledger marker (formal): `X ben/bat Y` (scribe language varies by city).
   - Example: **Marr, son of Marr**.

2) **House Gentilic** — “X [House-i]”
   - Elite/merchant **house-name** formed with **-i** (or **-i/-e** variants by dialect) meaning “of the house/line of”.
   - Signals blood **or adoption/service** to a founding name.
   - Example: **Nerise Zambrani** (“of House Zambran”).

3) **Demonym/People** — “X [People-an/-ian]”
   - Marks **origin or ethnicity** (esp. Kllrian, uplanders, islanders).
   - Used by outsiders and in courts for clarity; many keep it with pride.
   - Example: **Marak Kllrian** (“a Kllrian man”).

4) **Toponymic** — “X of [Place]”
   - Pilots, captains, and migrants in city-states.
   - Example: **Arsu of Seven Fingers**.

Epithets (“the Skin-Grass”) are **add-ons**, not replacements.

---

## Era drift (what to use when)
- **Early Ord (≤700 AO):** patronymic + toponymic dominate.
- **Zambranic (700–800):** **house gentilics** appear among elites (presses, contracts, temple registries).
- **Marrite (747–783):** no change; epithets flourish; censorship muddles records.
- **Restoration / Pax Ordica (≥790):** **ledger-names required** in port courts: choose one stable pattern (house/demonym/toponymic/patronymic). Insurance & Watch certificates prefer **house or demonym** for uniqueness.
- **Longara era (later):** fixed **family names** (often old house/demonym) become general in Koi-Hi and allied ports.

---

## Culture notes
- **Ordic houses:** The **-i** suffix tracks **belonging**, not strictly blood. Freedfolk and wards often retain a patron’s house-i as protection or pride (and list it as such in ledgers).
- **Kllrian names:** Demonyms are common; temple-service names replace or augment birth names during vows.
- **Sar names:** Toponymic “of [city]” stays fashionable; scholarly families sometimes add learned second elements (e.g., **Kelim Ar**), which function like short house tags.
- **Temple names:** Listeners and choirmasters may carry a **rite-name** in parallel (used in religious contexts only).

---

## How to write names in canon
- **First mention:** use the person’s **ledger-name** (house/demonym/toponymic/patronymic as appropriate) + any famous epithet:  
  *Nerise Zambrani (matron), Marr “the Skin-Grass”, Marak Kllrian, Arsu of Seven Fingers.*
- **After that:** shorten to **given name** (or epithet in narrative) unless there’s ambiguity.
- **In YAML front matter:** include a `naming:` block so future tools can format correctly.

### Front matter snippet (recommended)
```yaml
naming:
  style: house_gentilic | demonym | toponymic | patronymic
  components:
    given: Nerise
    house: Zambran        # house_gentilic
    people: Kllrian       # demonym
    place: Seven Fingers  # toponymic
    parent: Marr          # patronymic
  epithets: ["the Skin-Grass"]
  ledger_name: Nerise Zambrani
  street_names: ["Nerise", "Matron Nerise"]
