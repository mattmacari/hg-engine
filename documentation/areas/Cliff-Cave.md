# Cliff Cave

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D50R0101_CLIFF_CAVE` (`data/Encounters.c:8309`)
- **Map constant:** `MAP_D50R0101` (`include/constants/maps.h:346`)
- **Connects:** Route 47 (cave passage between the route's lower and upper sections).
- **Leads toward:** Optional side area, off the critical path. It is reachable from Cianwood City via Cliff Edge Gate,
  which puts it in the Chuck → Jasmine window.
- **Biome Map tie-in:** relevant to Jasmine's counter-access (Machop/Machoke for Fighting) and a
  wild preview of her signature mon (Onix/Steelix).

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 0 | No |
| Rock Smash | 30 | Yes |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 22 | Woobat | Woobat | Woobat |
| 2 | 20 | 19 | Geodude | Geodude | Geodude |
| 3 | 10 | 20 | Shellder | Shellder | Shellder |
| 4 | 10 | 22 | Corsola | Corsola | Corsola |
| 5 | 10 | 19 | Machop | Machop | Machop |
| 6 | 10 | 20 | Onix | Onix | Onix |
| 7 | 5 | 18 | Wooper | Wooper | Woobat |
| 8 | 5 | 20 | Quagsire | Quagsire | Misdreavus |
| 9 | 4 | 20 | Graveler | Graveler | Swoobat |
| 10 | 4 | 22 | Machoke | Machoke | Machoke |
| 11 | 1 | 23 | Steelix | Steelix | Steelix |
| 12 | 1 | 23 | Steelix | Steelix | Steelix |

## Water/rod tables

**Rock Smash (rate 30):** Shellder (20–26), Corsola (28–31).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

## Swarm

- `landSwarm = SPECIES_WOOBAT`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk | Morning/Day/Night |
| Graveler | Rock/Ground | 31 | Walk | Morning/Day |
| Wooper | Water/Ground | 49 | Walk | Morning/Day |
| Quagsire | Water/Ground | 50 | Walk | Morning/Day |
| Onix | Rock/Ground | 55 | Walk | Morning/Day/Night |
| Steelix | Steel/Ground | 56 | Walk | Morning/Day/Night |
| Machop | Fighting | 106 | Walk | Morning/Day/Night |
| Machoke | Fighting | 107 | Walk | Morning/Day/Night |
| Shellder | Water | 127 | Walk, Rock Smash | Morning/Day/Night |
| Corsola | Water/Rock | 129 | Walk, Rock Smash | Morning/Day/Night |
| Misdreavus | Ghost | 167 | Walk | Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk, Swarm (land) | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Zubat/Golbat replaced:** Golbat (slot 1, plus the inert land swarm) and night-only
  Zubat (slot 7) → **Woobat**, night-only Golbat (slot 9) → **Swoobat** (dex #276/#277). Route 36
  already uses Woobat as its cave-bat stand-in.
- **Resolved — Krabby/Kingler replaced** in both walk slots and Rock Smash: Krabby → **Shellder**,
  Kingler → **Corsola**. That follows the Cianwood precedent of Krabby → Shellder. Corsola
  (Water/Rock, #129) replaces Kingler instead of Cloyster, because a Water Stone evolution at
  level 22–31 would be out of place.
- **Left as-is:** dex-less rustling-grass species (Makuhita, Bronzor, Chingling) — post-game only.
