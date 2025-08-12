---
id: SYS-TECH-TV-14
name: Broadcast & Color Standard — Last War Aftermath Overlay
status: Draft
links:
  censors: canon/entities/factions/censors_bench.md
  law: canon/systems/governance/law_admin.md
  modern: canon/systems/transport/modern_index.md
---

## Standard OBR-625/50-P (Empire-wide)
- **Picture geometry.** 625 lines, interlaced; 50 fields/sec; 25 frames/sec.
- **Video modulation.** VSB-AM for video; FM for audio on a standard offset subcarrier.
- **Baseband signal.** Composite **Y** (luminance) + sync; **PAL-like** color with U/V phase alternation line-by-line.
- **Color subcarrier.** ~4.43 MHz; line-start **color burst** for phase reference.
- **Channel plan.** VHF + UHF allocations; guard bands sized for coastal ducting and bloom-season noise.

## Studio & transmission notes
- **Sync/Genlock.** One house black-burst reference per station; vectorscope + waveform monitor required.
- **Encoding.** RGB → YUV → PAL-like encoder; maintain 75% bars and a color test card for alignment.
- **Links.** Coax, microwave relays, or buried runs; hill-site relays for bays/valleys.
- **QC.** Hourly hue/sat checks; weekly full alignment; seasonal **bloom advisories** (filter/seal maintenance).

## Receiver realities (why pictures look “radioshack”)
- **Power instability.** Expect brownouts; recommend set-top stabilizers and battery inverters.
- **Hybrid sets.** Tube RF front-ends + transistor IF stages common; repair via module swaps/flyback replacements.
- **Antenna discipline.** Urban rabbit ears + UHF loops; rural community masts feeding splitters.
- **Color drift.** Weather, connectors, and room heat cause chroma noise and tint shifts; service cards circulated via guild.

## Governance & licensing
- **Spectrum & content.** The **Censors’ Bench** licenses channels and enforces decency/safety codes via fines and license points.
- **Interoperability.** OBR-625/50-P is mandatory for civil stations; military may transcode for secure nets.
