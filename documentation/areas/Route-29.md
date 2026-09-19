# Route 29

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R29_ROUTE_29` (`data/Encounters.c:109`)
- **Map constant:** `MAP_R29` (`include/constants/maps.h:37`)
- **Connects:** New Bark Town ↔ Cherrygrove City
- **Leads toward:** Falkner (Violet City) — first leg of the New Bark → Cherrygrove → Route 30 →
  Route 31 → Violet City path.
- **Biome Map tie-in:** none directly — `HACK_PLAN.md`'s Biome Map table starts its Falkner
  counter-access notes at Route 30/31/Dark Cave, not Route 29. Currently vanilla
  pastoral/grassland flavor (Pidgey/Sentret/Hoothoot).

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

No water tile access on this route — all fishing/surf slots are `{0, 0, SPECIES_NONE}`.

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 2 | Pidgey | Pidgey | Hoothoot |
| 2 | 20 | 3 | Sentret | Sentret | Hoothoot |
| 3 | 10 | 2 | Pidgey | Pidgey | Hoothoot |
| 4 | 10 | 3 | Sentret | Sentret | Hoothoot |
| 5 | 10 | 3 | Pidgey | Pidgey | Hoothoot |
| 6 | 10 | 3 | Pidgey | Pidgey | Hoothoot |
| 7 | 5 | 2 | Sentret | Sentret | Sentret |
| 8 | 5 | 2 | Sentret | Sentret | Sentret |
| 9 | 4 | 4 | Sentret | **Cutiefly** | Sentret |
| 10 | 4 | 4 | Pidgey | Pidgey | Hoothoot |
| 11 | 1 | 4 | Pidgey | **Cutiefly** | Sentret |
| 12 | 1 | 4 | Pidgey | Pidgey | Hoothoot |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_PIDGEY`
- `surfSwarm = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`
- **Inert:** `MAP_R29` is not in `sSwarmMapLUT` (`src/swarms.c`) — the 20-map daily-swarm rotation
  never lands here, so `landSwarm` currently does nothing.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day/Night |
| Sentret | Normal | 15 | Walk | Morning/Day/Night |
| Cutiefly | Bug/Fairy | 344 | Walk | Day only |
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Resolved — Rattata → Cutiefly:** Rattata (dex-less after curation) has been fully removed
  from this table. Day slots 9 & 11 (the two Rattata slots) now roll Cutiefly (added to
  `data/RegionalDex.c`, currently #344) — Bug/Fairy fits the pastoral/meadow read of the route
  and ties into the hack's Fairy-type presence. Cutiefly is **day-only**: it does not appear in
  the Morning or Night pools. The Morning slots 9 & 11 and Night slots 7, 8, 9 & 11 that Rattata
  also occupied were backfilled with the route's existing Pidgey/Sentret/Hoothoot pool (Sentret
  for all of them, extending Sentret into the night pool for the first time on this route — Pidgey
  stays diurnal, Hoothoot stays nocturnal).
- **Swarm field is dead weight as-is** — see Swarm section. Not worth touching unless Route 29
  is deliberately added to `sSwarmMapLUT`, which is source-code (not data-file) territory.
- **Type-coverage relevance (Pillar 3):** Falkner is Flying-type; Rock/Electric/Ice are the
  counters. Route 29 currently only offers Electric, and only via the rustling-grass slots
  (Plusle/Minun/Shinx) rather than the main land table — worth factoring into the audit once
  Route 30/31/Dark Cave (the areas the Biome Map actually calls out for this) are documented too.
- Slot 9 and 11 level jump (2/3 → 4) for the uncommon/rare slots is standard vanilla shaping
  (rarer slots skew a level or two higher) — not itself a problem, just worth knowing the pattern
  before rebalancing.
- Regional dex total is now 366, after syncing `data/RegionalDex.c` to the curation sheet's full
  `keep` decisions (see commit history) — `HACK_PLAN.md`'s Open Decisions no longer tracks a fixed
  ceiling number; the sheet's per-species decisions are the source of truth.
