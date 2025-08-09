# Diegetic Documents

Use for in-universe texts (museum labels, doc scripts, hymn fragments).

Template header:

---
fact_box:
  title: ""                # in-universe title on the page
  doc_type: pamphlet       # pamphlet | transcript | schoolbook | poster | letter | hymn | law | logbook | newspaper
  author_in_universe: ""   # or 'unknown'
  date_ao: 0               # integer AO if known, else null
  era: ERA-100             # one of your era IDs
  relates_to: [EVT-0518-BOM, LOC:ORD-001]   # event/place/person IDs
  location_ids: []         # if it’s “from” a place (publisher, temple, school)
  audience: public         # public | elite | military | temple | children
  reliability: medium      # low | medium | high (how much we trust it)
  source_tier: primary     # primary | secondary | reconstruction
  claims:
    - ""                   # 2–6 concise factual claims this text makes
  contradictions: []       # known disputes this text raises
  canonical_links: []      # pointers to canon files: eras/.., systems/..
---
