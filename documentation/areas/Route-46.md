# Route 46

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R46_ROUTE_46` (`data/Encounters.c:6809`)
- **Map constant:** `MAP_R46` (`include/constants/maps.h:52`)
- **Connects:** Route 29 (south) ↔ Route 45 (north, one-way ledges down from Blackthorn).
- **Leads toward:** Falkner — the short section reachable from Route 29 is an early-game side
  area (Lv2–4). The northern part is only reachable later, coming down from Route 45.

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
| 1 | 20 | 3 | Geodude | Geodude | Geodude |
| 2 | 20 | 2 | Pidgey | Pidgey | Sentret |
| 3 | 10 | 3 | Geodude | Geodude | Geodude |
| 4 | 10 | 2 | Pidgey | Pidgey | Sentret |
| 5 | 10 | 2 | Sentret | Sentret | Sentret |
| 6 | 10 | 2 | Sentret | Sentret | Sentret |
| 7 | 5 | 2 | Geodude | Geodude | Geodude |
| 8 | 5 | 2 | Geodude | Geodude | Geodude |
| 9 | 4 | 3 | Pidgey | Pidgey | Geodude |
| 10 | 4 | 4 | Sentret | Sentret | Sentret |
| 11 | 1 | 3 | Pidgey | Pidgey | Geodude |
| 12 | 1 | 4 | Sentret | Sentret | Sentret |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_GEODUDE`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day |
| Sentret | Normal | 15 | Walk | Morning/Day/Night |
| Geodude | Rock/Ground | 30 | Walk, Swarm (land) | Morning/Day/Night |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** Missed in the original Falkner
  pass:
  - Spearow → **Pidgey** (#10).
  - Rattata → **Sentret** (#15), including the night slots.
  - This matches Route 29's own table next door. Geodude (and its land swarm) is unchanged.
