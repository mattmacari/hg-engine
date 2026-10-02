# Dark Cave (Route 45 entrance)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D42R0101_DARK_CAVE_ROUTE_45_ENTRANCE` (`data/Encounters.c:7009`)
- **Map constant:** `MAP_D42R0101` (`include/constants/maps.h:127`)
- **Connects:** Route 45 (east), and the deeper side of Dark Cave toward the Route 31 entrance.
- **Leads toward:** optional side area in the Clair window (off Route 45).

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 23 | Geodude | Geodude | Geodude |
| 2 | 20 | 23 | Woobat | Woobat | Woobat |
| 3 | 10 | 23 | Geodude | Geodude | Geodude |
| 4 | 10 | 23 | Woobat | Woobat | Woobat |
| 5 | 10 | 25 | Graveler | Graveler | Graveler |
| 6 | 10 | 25 | Graveler | Graveler | Graveler |
| 7 | 5 | 20 | Wobbuffet | Wobbuffet | Wobbuffet |
| 8 | 5 | 20 | Wobbuffet | Wobbuffet | Wobbuffet |
| 9 | 4 | 25 | Wobbuffet | Wobbuffet | Wobbuffet |
| 10 | 4 | 23 | Swoobat | Swoobat | Swoobat |
| 11 | 1 | 25 | Wobbuffet | Wobbuffet | Wobbuffet |
| 12 | 1 | 23 | Swoobat | Swoobat | Swoobat |

## Water/rod tables

**Surf (rate 10):** Magikarp (10–20), Magikarp (5–15), Magikarp (2–10), Magikarp (2–10), Magikarp (2–10).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Wooper (10), Wooper (10).
**Good Rod (rate 50):** Magikarp (20), Wooper (20), Wooper (20), Wooper (20), Wooper (20).
**Super Rod (rate 75):** Wooper (40), Wooper (40), Magikarp (40), Quagsire (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

## Swarm

- `landSwarm = SPECIES_GEODUDE`, `surfSwarm = SPECIES_MAGIKARP`, `nightFish = SPECIES_WOOPER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk, Swarm (land) | Morning/Day/Night |
| Graveler | Rock/Ground | 31 | Walk | Morning/Day/Night |
| Wooper | Water/Ground | 49 | Fish, Fish (night) | — |
| Quagsire | Water/Ground | 50 | Fish | — |
| Magikarp | Water | 65 | Surf, Fish, Swarm (surf), Swarm (fish) | — |
| Wobbuffet | Psychic | 85 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 374 entries (Horsea/Seadra/Kingdra/Swablu/Altaria added as #370–374 in the Clair pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Goldeen/Seaking → Wooper/Quagsire** on every rod slot plus the night fish. This
  mirrors the fix on this cave's other side (Dark-Cave-Route-31-Entrance.md), so the whole cave
  shares one water pool.
- **Resolved — Zubat/Golbat → Woobat/Swoobat**, the same cave-bat stand-in as Cliff Cave and Mt.
  Mortar.
  - This differs from the earlier Falkner-era pass, which deliberately kept Zubat dex-less in this
    cave's Route 31 side (and in Union Cave/Slowpoke Well) because the Zubat line is `keep=No`.
  - The early caves still have Zubat. Chuck's Flying counter-access relies on that early Zubat,
    so changing them would need a fresh decision.
- **Left as-is:** dex-less rustling-grass species (post-game only).
