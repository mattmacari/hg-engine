# Route 43

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R43_ROUTE_43` (`data/Encounters.c:5709`)
- **Map constant:** `MAP_R43` (`include/constants/maps.h:49`)
- **Connects:** Mahogany Town (south) ↔ Lake of Rage (north).
- **Leads toward:** Pryce — the Lake of Rage / Rocket Hideout story beat on this route has to be
  cleared before Mahogany's gym opens.
- **Biome Map tie-in:** none directly; grassland with a Mareep/Flaaffy/Girafarig core.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 20 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 20)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 15 | Flaaffy | Flaaffy | Flaaffy |
| 2 | 20 | 15 | Girafarig | Girafarig | Girafarig |
| 3 | 10 | 15 | Flaaffy | Flaaffy | Flaaffy |
| 4 | 10 | 15 | Girafarig | Girafarig | Girafarig |
| 5 | 10 | 17 | Pidgeotto | Pidgeotto | Noctowl |
| 6 | 10 | 17 | Pidgeotto | Pidgeotto | Noctowl |
| 7 | 5 | 15 | Mareep | Mareep | Spinarak |
| 8 | 5 | 15 | Mareep | Mareep | Spinarak |
| 9 | 4 | 16 | Ledyba | Flaaffy | Mareep |
| 10 | 4 | 17 | Pidgeotto | Flaaffy | Spinarak |
| 11 | 1 | 16 | Ledyba | Flaaffy | Mareep |
| 12 | 1 | 17 | Pidgeotto | Flaaffy | Spinarak |

## Water/rod tables

**Surf (rate 10):** Magikarp (15–25), Magikarp (10–20), Magikarp (5–15), Magikarp (5–15), Magikarp (50).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Poliwag (10), Poliwag (10).
**Good Rod (rate 50):** Magikarp (20), Poliwag (20), Poliwag (20), Poliwag (20), Poliwag (20).
**Super Rod (rate 75):** Poliwag (40), Poliwag (40), Magikarp (40), Poliwag (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_FLAAFFY`, `surfSwarm = SPECIES_MAGIKARP`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgeotto | Normal/Flying | 11 | Walk | Morning/Day |
| Noctowl | Normal/Flying | 14 | Walk | Night |
| Ledyba | Bug/Flying | 26 | Walk | Morning |
| Spinarak | Bug/Poison | 28 | Walk | Night |
| Mareep | Electric | 46 | Walk | Morning/Day/Night |
| Flaaffy | Electric | 47 | Walk, Swarm (land) | Morning/Day/Night |
| Magikarp | Water | 65 | Surf, Fish, Swarm (surf), Swarm (fish) | — |
| Girafarig | Normal/Psychic | 111 | Walk | Morning/Day/Night |
| Poliwag | Water | 346 | Fish, Fish (night) | — |
| Bidoof | Normal | **not in dex** | Rustling grass (Sinnoh) | — |
| Buizel | Water | **not in dex** | Rustling grass (Sinnoh) | — |
| Linoone | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Whismur | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in the Jasmine-corridor pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Venonat replaced by time of day:**
  - Morning slots 9/11 (5%) → **Ledyba** (#26, the canon morning bug).
  - Night slots 7/8/10/12 (15%) → **Spinarak** (#28, the canon night bug).
  - Day was already Venonat-free.
- **Left as-is:** dex-less rustling-grass species (post-game only).
