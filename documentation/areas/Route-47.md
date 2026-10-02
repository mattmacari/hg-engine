# Route 47

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R47_ROUTE_47` (`data/Encounters.c:7109`)
- **Map constant:** `MAP_R47` (`include/constants/maps.h:155`)
- **Connects:** Cliff Edge Gate (east, → Cianwood City) ↔ Route 48 (north); Cliff Cave opens off it.
- **Leads toward:** Optional side area, off the critical path. It is reachable from Cianwood City via Cliff Edge Gate,
  which puts it in the Chuck → Jasmine window. Walk levels (31–40) run well above the gym, so it plays as an over-leveled
  side route.
- **Biome Map tie-in:** none directly. It's a coastal cliff route, so the rework leans seabird +
  ocean, consistent with the Cianwood marine pool.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 35 | Farfetch’d | Farfetch’d | Noctowl |
| 2 | 20 | 35 | Miltank | Miltank | Miltank |
| 3 | 10 | 34 | Ditto | Ditto | Ditto |
| 4 | 10 | 33 | Ditto | Ditto | Ditto |
| 5 | 10 | 32 | Ditto | Ditto | Ditto |
| 6 | 10 | 31 | Ditto | Ditto | Ditto |
| 7 | 5 | 32 | Gloom | Gloom | Gloom |
| 8 | 5 | 31 | Wingull | Wingull | Wingull |
| 9 | 4 | 34 | Pelipper | Pelipper | Pelipper |
| 10 | 4 | 31 | Tauros | Tauros | Tauros |
| 11 | 1 | 33 | Tauros | Tauros | Tauros |
| 12 | 1 | 40 | Ditto | Ditto | Ditto |

## Water/rod tables

**Surf (rate 15):** Chinchou (15–25), Seel (10–20), Staryu (15–25), Staryu (15–25), Staryu (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Chinchou (10), Chinchou (10).
**Good Rod (rate 50):** Magikarp (20), Chinchou (20), Chinchou (20), Shellder (20), Chinchou (20).
**Super Rod (rate 75):** Chinchou (40), Shellder (40), Lanturn (40), Lanturn (40), Lanturn (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_DITTO`, `surfSwarm = SPECIES_CHINCHOU`, `nightFish = SPECIES_SHELLDER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Active (land only):** `MAP_R47` is in `sSwarmMapLUT` (`src/swarms.c:28`, `SWARM_GRASS`) — the Ditto land swarm fires; the surf/fish swarm fields are inert.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Noctowl | Normal/Flying | 14 | Walk | Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Gloom | Grass/Poison | 69 | Walk | Morning/Day/Night |
| Ditto | Normal | 75 | Walk, Swarm (land) | Morning/Day/Night |
| Miltank | Normal | 112 | Walk | Morning/Day/Night |
| Farfetch’d | Normal/Flying | 120 | Walk | Morning/Day |
| Staryu | Water | 125 | Surf | — |
| Shellder | Water | 127 | Fish, Fish (night) | — |
| Chinchou | Water/Electric | 132 | Surf, Fish, Swarm (surf) | — |
| Lanturn | Water/Electric | 133 | Fish | — |
| Seel | Water | 134 | Surf | — |
| Wingull | Water/Flying | 209 | Walk | Morning/Day/Night |
| Pelipper | Water/Flying | 210 | Walk | Morning/Day/Night |
| Tauros | Normal | 369 | Walk | Morning/Day/Night |
| Bidoof | Normal | **not in dex** | Rustling grass (Sinnoh) | — |
| Buizel | Water | **not in dex** | Rustling grass (Sinnoh) | — |
| Linoone | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Whismur | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Correction:** `Cianwood-City.md` previously called Route 47/48 "deep post-Mt.-Silver Kanto".
  That's wrong — they're Johto routes west of Cianwood, and their wild levels (Route 48 is 20–25,
  Cliff Cave 18–23) fit this point in the game. The Chuck Fairy-access conclusion doesn't change,
  because neither route has a Fairy type anyway.
- **Resolved — dex-less land species replaced:** Spearow (slot 8) → **Wingull**, Fearow (slot 9) →
  **Pelipper**, Raticate (slots 10/11) → **Tauros** (now dex #369, keeps the Miltank pairing from
  slot 2). Wingull/Pelipper are dex-tracked (#209/#210) and otherwise only appear in Vermilion.
- **Resolved — Tentacool/Tentacruel replaced** across surf, every rod tier, and `surfSwarm`:
  Tentacool → **Chinchou**, Tentacruel → **Lanturn**. Chinchou/Lanturn were already this route's
  rod species, so this deepens the existing local pool instead of importing Staryu again.
- **Left as-is:** dex-less rustling-grass species (Whismur, Linoone, Buizel, Bidoof). Sound
  species are post-game only and out of scope for Phase 1 passes.
