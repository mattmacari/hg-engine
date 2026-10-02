# Route 48

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R48_ROUTE_48` (`data/Encounters.c:10209`)
- **Map constant:** `MAP_R48` (`include/constants/maps.h:156`)
- **Connects:** Route 47 (south) ↔ Safari Zone Gate (north).
- **Leads toward:** Optional side area, off the critical path. It is reachable from Cianwood City via Cliff Edge Gate,
  which puts it in the Chuck → Jasmine window.
- **Biome Map tie-in:** none directly — open grassland on the approach to the Safari Zone.

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
| 1 | 20 | 25 | Farfetch’d | Farfetch’d | Growlithe |
| 2 | 20 | 20 | Tauros | Tauros | Tauros |
| 3 | 10 | 20 | Hoppip | Hoppip | Hoppip |
| 4 | 10 | 21 | Pidgeotto | Pidgeotto | Pidgeotto |
| 5 | 10 | 22 | Gloom | Gloom | Gloom |
| 6 | 10 | 24 | Gloom | Gloom | Gloom |
| 7 | 5 | 21 | Growlithe | Growlithe | Growlithe |
| 8 | 5 | 20 | Girafarig | Girafarig | Girafarig |
| 9 | 4 | 20 | Phanpy | Phanpy | Phanpy |
| 10 | 4 | 22 | Growlithe | Growlithe | Growlithe |
| 11 | 1 | 22 | Hoppip | Hoppip | Hoppip |
| 12 | 1 | 24 | Tauros | Tauros | Tauros |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_TAUROS`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgeotto | Normal/Flying | 11 | Walk | Morning/Day/Night |
| Hoppip | Grass/Flying | 60 | Walk | Morning/Day/Night |
| Gloom | Grass/Poison | 69 | Walk | Morning/Day/Night |
| Growlithe | Fire | 99 | Walk | Morning/Day/Night |
| Girafarig | Normal/Psychic | 111 | Walk | Morning/Day/Night |
| Farfetch’d | Normal/Flying | 120 | Walk | Morning/Day |
| Phanpy | Ground | 153 | Walk | Morning/Day/Night |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |
| Tauros | Normal | 369 | Walk, Swarm (land) | Morning/Day/Night |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Fearow (slot 4, 10%) → Pidgeotto** (dex #11), a straight bird-for-bird swap at the
  same level.
- **Resolved — Diglett (slot 9, 4%) → Phanpy** (dex #153). Phanpy suits the grassland and adds an
  optional Ground option before Jasmine. It otherwise only spawns on Route 45 and Mt. Silver.
- Tauros (slots 2/12 plus the inert land swarm) stays — now dex-tracked as #369.
