# Route 37

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R37_ROUTE_37` (`data/Encounters.c:2609`)
- **Map constant:** `MAP_R37` (`include/constants/maps.h:45`)
- **Connects:** Route 36 (south) ↔ Ecruteak City (north).
- **Leads toward:** Morty (Ecruteak City) — this short route is the final leg of the Morty approach.
  It was skipped in the Morty-corridor pass and documented later, during the Pryce pass.
- **Biome Map tie-in:** none directly; apricorn-tree woodland edge, same feel as Route 36.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 13 | Pidgey | Pidgey | Spinarak |
| 2 | 20 | 15 | Stantler | Stantler | Stantler |
| 3 | 10 | 13 | Pidgey | Pidgey | Spinarak |
| 4 | 10 | 15 | Stantler | Stantler | Stantler |
| 5 | 10 | 15 | Pidgey | Pidgey | Hoothoot |
| 6 | 10 | 15 | Pidgey | Pidgey | Hoothoot |
| 7 | 5 | 14 | Growlithe | Growlithe | Growlithe |
| 8 | 5 | 14 | Growlithe | Growlithe | Growlithe |
| 9 | 4 | 15 | Pidgey | Pidgeotto | Spinarak |
| 10 | 4 | 15 | Pidgey | Growlithe | Spinarak |
| 11 | 1 | 15 | Pidgey | Pidgeotto | Spinarak |
| 12 | 1 | 15 | Pidgey | Growlithe | Spinarak |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_PIDGEY`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk, Swarm (land) | Morning/Day |
| Pidgeotto | Normal/Flying | 11 | Walk | Day |
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Spinarak | Bug/Poison | 28 | Walk | Night |
| Growlithe | Fire | 99 | Walk | Morning/Day/Night |
| Stantler | Normal | 101 | Walk | Morning/Day/Night |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in the Jasmine-corridor pass) —
re-`grep` if the dex is renumbered.

## Notes

- Already clean — every species is dex-tracked, no changes made.
- Growlithe (slots 7/8 all day, plus slots 10/12 by day) is another pre-Morty Fire source alongside
  Route 33/36, and it stays relevant for Jasmine's Fire coverage.
- Correction: `Route-36.md` previously described Route 37 as leading "onward past Ecruteak toward
  Olivine — not part of the approach to Morty". In fact Route 36 → Route 37 → Ecruteak is the main
  path. Route 36's header has been fixed to match.
