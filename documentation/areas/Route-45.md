# Route 45

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R45_ROUTE_45` (`data/Encounters.c:6709`)
- **Map constant:** `MAP_R45` (`include/constants/maps.h:51`)
- **Connects:** Blackthorn City (north) ↔ Route 46 (south), with the Dark Cave entrance off it.
  Ledges make it effectively one-way going south.
- **Leads toward:** reachable from Blackthorn before Clair, so it's an optional side area in her
  window.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Clair row suggested a Fairy option on "a wilder
  mountain-forest approach". That's covered elsewhere now (see the Clair row's counter-access
  note), so this route's role is Dragon access via the Swablu swarm.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 23 | Geodude | Geodude | Geodude |
| 2 | 20 | 23 | Graveler | Graveler | Graveler |
| 3 | 10 | 23 | Geodude | Geodude | Geodude |
| 4 | 10 | 23 | Graveler | Graveler | Graveler |
| 5 | 10 | 24 | Gligar | Gligar | Gligar |
| 6 | 10 | 24 | Gligar | Gligar | Gligar |
| 7 | 5 | 20 | Phanpy | Phanpy | Phanpy |
| 8 | 5 | 20 | Phanpy | Phanpy | Phanpy |
| 9 | 4 | 25 | Graveler | Graveler | Graveler |
| 10 | 4 | 27 | Graveler | Graveler | Graveler |
| 11 | 1 | 25 | Graveler | Graveler | Graveler |
| 12 | 1 | 27 | Graveler | Graveler | Graveler |

## Water/rod tables

**Surf (rate 10):** Magikarp (15–25), Magikarp (10–20), Magikarp (2–10), Magikarp (2–10), Magikarp (2–10).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Poliwag (10), Poliwag (10).
**Good Rod (rate 50):** Magikarp (20), Poliwag (20), Poliwag (20), Poliwag (20), Poliwag (20).
**Super Rod (rate 75):** Poliwag (40), Poliwag (40), Magikarp (40), Poliwag (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_SWABLU`, `surfSwarm = SPECIES_MAGIKARP`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`.
- **Active (land only):** `MAP_R45` is in `sSwarmMapLUT` (`src/swarms.c:27`, `SWARM_GRASS`) — the Swablu land swarm fires here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk | Morning/Day/Night |
| Graveler | Rock/Ground | 31 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Surf, Fish, Swarm (surf), Swarm (fish) | — |
| Gligar | Ground/Flying | 146 | Walk | Morning/Day/Night |
| Phanpy | Ground | 153 | Walk | Morning/Day/Night |
| Poliwag | Water | 346 | Fish, Fish (night) | — |
| Swablu | Normal/Flying | 373 | Swarm (land) | — |
| Bidoof | Normal | **not in dex** | Rustling grass (Sinnoh) | — |
| Buizel | Water | **not in dex** | Rustling grass (Sinnoh) | — |
| Linoone | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Whismur | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 374 entries (Horsea/Seadra/Kingdra/Swablu/Altaria added as #370–374 in the Clair pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Swablu/Altaria added to the regional dex (#373/#374)** instead of replacing the
  swarm. The Swablu land swarm is active here (in the swarm LUT). Swablu evolves into Dragon-type
  Altaria at Lv35, which gives a Dragon counter-access path before Clair and fits Blackthorn's
  dragon-mountain flavor.
- The walking table was already clean. Gligar and Phanpy are this route's Ground types.
- **Left as-is:** dex-less rustling-grass species (post-game only).
