---
id: SNAP:LEXICON-950
name: Lexicon & Drift at the Apex (c. 950 AO)
status: Draft
links:
  apex: canon/notes/snapshots/empire_at_its_peak_c950.md
  ling_guide: canon/systems/language/linguistic_guide_for_ord_sar.md
  names: canon/systems/language/names_and_onomastics_for_ord_sar.md
  suffixes: canon/systems/language/onomastic_suffixes.md
  rhythm: canon/systems/religions/good_old_rhythm.md
---

> **Scope.** This is a writer’s cheat-sheet for how things are *called* c.950 AO, plus where they’re already drifting. It assumes a Cadence-wide administrative koiné (print era), with lively coastal vernaculars at the edges. Printing and temple schools suppress wild divergence—for now. 

## Registers you’ll see in text
- **Ledger/court name** (formal): appears on edicts, ledgers, seals.  
- **Temple/choir name** (ritual): the form choirs sing or temple minutes use.  
- **Street/port name** (vernacular): clipped, punning, or metonymic; varies by city.  
(See language system pages for naming scaffolds.) 

## Offices & institutions (koiné vs edges)
| Concept (gloss) | c.700 form | **c.950 koiné (use this)** | Edge/vernacular (documented) | Likely later drift |
|---|---|---|---|---|
| High Master (state head) | High Master | **High Master**; also metonym **the Oar-Bench** | “Bench-master” (Sar ports) | *Oarmaster*, *Bench* as sole headword |
| Council of Captains | Council of Captains | **Council (of Captains)** | “Sea Council” | “Captains’ Council” (legal narrowing) |
| Captain-Representative | Captain-Rep | **Captain-Representative** | “Rep-Captain”, “Captain-Post” | “Port-Rep” (treaty emphasis) |
| Synod of Beats | Synod of Beats | **Synod**; houses as **First–Sixth Beat** | “First House” etc. | Houses rebranded by functions (“Courts”, “Missions”) |
| Keeper of the Oboe Seal | Keeper of the Oboe Seal | **Keeper** (capitalized) | “Seal-keeper” | “Keeperate” (bureaucratic noun) |
| Censor’s Bench | Censor’s Bench | **Censor’s Bench** (narrow warrant) | “Bench” | “Censorate” (scope creep) |
| Harbor Watches | Harbor Watches | **Watches** | “Bell-men” (Kllrian arcs) | “Coast Guard” (loan calque) |
| Guild of Compositories | Compositories (Guild) | **Compository House(s)** / **Guild** | “Row” (metonym) | “Press Guilds” (genericization) |
| Treaty Port | Treaty Port | **Treaty Port** | “Accord Port”, “Ticket Port” | “Contract Port” (modern legalism) |
| Insurance Steps | Insurance Steps | **Steps** | “Claim-stairs” (Sar) | “Exchange Steps” (finance drift) |

(Relationships and canonical spellings align with the apex/known-world snapshots and Rhythm institutions.) 

## Religion & calendar terms
- **Good Old Rhythm** (ledger); **Old Bold Rhythm** (title of the recension); **the Old Song** (vernacular for the tideways & moral order). Use **Beat One/Six** (not “First House” in narration unless POV warrants). 
- **Hexennial Games** (ledger); street calls them **the Long Games** in some ports.  
- **Oboe** (the sun) is stable; **Hex** (the moon) is the common coastal spelling; formal schools sometimes mark **Ex**—treat **Ex** as deprecated alias in new pages. (Keep both in search aliases to preserve legacy hits.) 

## Civic & naval vocabulary (scene spice)
- **Beacon Leg(s)** (range lights) → “the **Chain**” when referring to a continuous run.  
- **War docket** (emergency legal mode).  
- **Convoy premium** (posted at the Steps).  
- **Boarder kit** (marine load-out); **watch cloak** (short, oiled). 

## Places & ethnonyms (orthography you’ll see)
- **Ord City**; **Koi-Hi** (legacy **Coi-Hi** survives on old pilot-books); **Seven Fingers** (trade mishearing that stuck).  
- **Kllrian** (people/arc); **Sar-North**, **Ord-Bay** (ledger hyphenation).  
(Prefer the koiné forms in narration; keep legacy spellings in doc `aliases:`.)  

## Names & onomastics (quick cues)
- **House gentilic**: _Nerise Zambrani_.  
- **Demonym**: _Marak Kllrian_.  
- **Toponymic**: _Arsu of Seven Fingers_.  
Use **ledger_name** in front-matter; allow local short forms in POV. (See language pages.) 

## Pronunciation notes (stage directions, not IPA)
- **Oboe** = OH-boh; **Hex** = like “hex.”  
- **Compository** = com-POS-i-tory (printer-editor house).  
- **Kllrian** = KLIH-ree-an (light double-L).  
- **Zambrani** = zam-BRAH-nee (house gentilic stress on -bra-).

## How to record drift in docs (lightweight pattern)
When a term already shows variants, add an alias map in front-matter on the *base* page:
```yaml
aliases_by_era:
  05xx-0599: ["Ex"]        # early coastal school orthography
  0860-1050: ["Hex"]       # koiné standard at apex
  1700-1803: ["Hex","Hexe"]# modern spellings seen in pamphlets
