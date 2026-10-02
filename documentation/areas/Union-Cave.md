# Union Cave (1F / B1F / B2F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers all three floors in one doc since they share the same species pool with only
levels/slot-arrangement shifting per floor (see Land encounter table below) — not identical enough
to fully collapse like Sprout Tower's floors, so each floor gets its own table.

## Header facts

- **ENCDATA constants:**
  - `ENCDATA_D25R0101_UNION_CAVE_1F` (`data/Encounters.c:1409`)
  - `ENCDATA_D25R0102_UNION_CAVE_B1F` (`data/Encounters.c:1509`)
  - `ENCDATA_D25R0103_UNION_CAVE_B2F` (`data/Encounters.c:1609`)
- **Map constants:** `MAP_D25R0101` (`include/constants/maps.h:103`),
  `MAP_D25R0102` (`include/constants/maps.h:157`), `MAP_D25R0103` (`include/constants/maps.h:158`)
- **Connects:** an underground path between Route 32 (north entrance, near the Ruins of Alph
  turnoff) and Route 33 (south exit) — runs roughly parallel to the surface path.
- **Leads toward:** Bugsy (Azalea Town) — mid-leg of the approach.
- **Biome Map tie-in:** not named directly in `HACK_PLAN.md`'s Bugsy row (which centers on Ilex
  Forest and the Fire/Flying/Rock counter-access note). This is a Rock/Ground cave biome, so it's
  more relevant as a *counter-access* source for later Rock-weak fights than as Bugsy's own theme.

## 1F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 6 | Geodude | Geodude | Geodude |
| 2 | 20 | 6 | Sandshrew | Sandshrew | Sandshrew |
| 3 | 10 | 6 | Geodude | Geodude | Geodude |
| 4 | 10 | 6 | Sandshrew | Sandshrew | Sandshrew |
| 5 | 10 | 5 | Woobat | Woobat | Woobat |
| 6 | 10 | 5 | Woobat | Woobat | Woobat |
| 7 | 5 | 4 | Dunsparce | Dunsparce | Dunsparce |
| 8 | 5 | 4 | Dunsparce | Dunsparce | Dunsparce |
| 9 | 4 | 7 | Woobat | Woobat | Woobat |
| 10 | 4 | 6 | Onix | Onix | Onix |
| 11 | 1 | 7 | Woobat | Woobat | Woobat |
| 12 | 1 | 6 | Onix | Onix | Onix |

### Water/rod tables

**Surf (rate 15):** Wooper (10–20), Quagsire (15–25), Quagsire (10–20), Quagsire (10–20), Quagsire (10–20).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Wooper (10), Wooper (10).
**Good Rod (rate 50):** Magikarp (20), Wooper (20), Wooper (20), Wooper (20), Wooper (20).
**Super Rod (rate 75):** Wooper (40), Wooper (40), Magikarp (40), Quagsire (40), Magikarp (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_GEODUDE`, `surfSwarm = SPECIES_WOOPER`, `nightFish = SPECIES_WOOPER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk, Swarm (land) | Morning/Day/Night |
| Sandshrew | Ground | 41 | Walk | Morning/Day/Night |
| Dunsparce | Normal | 45 | Walk | Morning/Day/Night |
| Wooper | Water/Ground | 49 | Surf, Fish, Swarm (surf), Fish (night) | — |
| Quagsire | Water/Ground | 50 | Surf, Fish | — |
| Onix | Rock/Ground | 55 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B1F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 15 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 15)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 8 | Geodude | Geodude | Geodude |
| 2 | 20 | 8 | Sandshrew | Sandshrew | Sandshrew |
| 3 | 10 | 8 | Geodude | Geodude | Geodude |
| 4 | 10 | 8 | Sandshrew | Sandshrew | Sandshrew |
| 5 | 10 | 7 | Woobat | Woobat | Woobat |
| 6 | 10 | 7 | Woobat | Woobat | Woobat |
| 7 | 5 | 8 | Onix | Onix | Onix |
| 8 | 5 | 8 | Onix | Onix | Onix |
| 9 | 4 | 9 | Woobat | Woobat | Woobat |
| 10 | 4 | 6 | Dunsparce | Dunsparce | Dunsparce |
| 11 | 1 | 9 | Woobat | Woobat | Woobat |
| 12 | 1 | 6 | Dunsparce | Dunsparce | Dunsparce |

### Water/rod tables

**Surf (rate 15):** Wooper (10–20), Quagsire (15–25), Quagsire (10–20), Quagsire (10–20), Quagsire (10–20).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Wooper (10), Wooper (10).
**Good Rod (rate 50):** Magikarp (20), Wooper (20), Wooper (20), Wooper (20), Wooper (20).
**Super Rod (rate 75):** Wooper (40), Wooper (40), Magikarp (40), Quagsire (40), Magikarp (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_GEODUDE`, `surfSwarm = SPECIES_WOOPER`, `nightFish = SPECIES_WOOPER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk, Swarm (land) | Morning/Day/Night |
| Sandshrew | Ground | 41 | Walk | Morning/Day/Night |
| Dunsparce | Normal | 45 | Walk | Morning/Day/Night |
| Wooper | Water/Ground | 49 | Surf, Fish, Swarm (surf), Fish (night) | — |
| Quagsire | Water/Ground | 50 | Surf, Fish | — |
| Onix | Rock/Ground | 55 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B2F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 15 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 15)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 22 | Woobat | Woobat | Woobat |
| 2 | 20 | 22 | Dunsparce | Dunsparce | Dunsparce |
| 3 | 10 | 22 | Woobat | Woobat | Woobat |
| 4 | 10 | 22 | Dunsparce | Dunsparce | Dunsparce |
| 5 | 10 | 22 | Swoobat | Swoobat | Swoobat |
| 6 | 10 | 22 | Swoobat | Swoobat | Swoobat |
| 7 | 5 | 21 | Geodude | Geodude | Geodude |
| 8 | 5 | 21 | Geodude | Geodude | Geodude |
| 9 | 4 | 20 | Dunsparce | Dunsparce | Dunsparce |
| 10 | 4 | 23 | Onix | Onix | Onix |
| 11 | 1 | 20 | Dunsparce | Dunsparce | Dunsparce |
| 12 | 1 | 23 | Onix | Onix | Onix |

### Water/rod tables

**Surf (rate 15):** Staryu (10–20), Quagsire (15–25), Starmie (15–25), Starmie (15–25), Starmie (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Shellder (10), Shellder (10).
**Good Rod (rate 50):** Magikarp (20), Shellder (20), Shellder (20), Corsola (20), Shellder (20).
**Super Rod (rate 75):** Shellder (40), Corsola (40), Shellder (40), Cloyster (40), Shellder (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_WOOBAT`, `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_STARYU`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk | Morning/Day/Night |
| Dunsparce | Normal | 45 | Walk | Morning/Day/Night |
| Quagsire | Water/Ground | 50 | Surf | — |
| Onix | Rock/Ground | 55 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Staryu | Water | 125 | Surf, Swarm (surf), Fish (night) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water | 127 | Fish | — |
| Cloyster | Water/Ice | 128 | Fish | — |
| Corsola | Water/Rock | 129 | Fish | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk, Swarm (land) | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


Dex numbers as of `data/RegionalDex.c` with 377 entries — re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** Every dex-less species is
  replaced:
  - Zubat/Golbat → **Woobat/Swoobat** (#276/#277), including B2F's inert land swarm.
  - Rattata/Raticate → **Dunsparce** (#45), the cave dweller from Dark Cave.
  - Goldeen/Seaking (1F/B1F rods) → **Wooper/Quagsire**, matching Dark Cave's water.
  - B2F's sea-connected water: Tentacool/Tentacruel → **Staryu/Starmie**, Krabby/Kingler →
    **Shellder/Cloyster** (the Cianwood mapping).
  - Chuck's Flying counter-access that cited Union Cave Zubat now comes from Woobat (Psychic/Flying).
  Earlier notes below that describe these species as dex-less or intentionally kept are superseded.
- Zubat/Golbat/Rattata/Raticate/Goldeen/Seaking/Tentacool/Tentacruel/Krabby/Kingler dex-less here
  is the same routine curation-sheet cut convention as the other Falkner/Bugsy-approach docs
  (`keep = No` in `data/generated/species_dex_meta.csv`) — not a bug. Notably this leaves the whole
  B2F fishing table (Krabby/Corsola/Kingler minus Corsola) and most of B2F's land table dex-less;
  Geodude/Onix/Quagsire are the only dex-tracked land species on that floor.
- **Type-coverage relevance (Pillar 3):** this cave is a genuine pre-Bugsy **Rock** source
  (Geodude/Onix, both dex-tracked, all three floors) — Rock isn't one of Bugsy's own needed
  counters (Bugsy is Bug-type; Fire/Flying/Rock are what the player needs *against* Bugsy, not
  what Bugsy needs against the player), so this doesn't close Bugsy's own audit, but it's worth
  remembering as an available Rock-type pickup on this leg for whichever *later* gym's audit needs
  it (Rock is a recurring "needed counter" elsewhere in the Biome Map, e.g. Falkner's row already
  used Geodude from Dark Cave/Route 31 for the same reason).
- No Fire or Flying-that-isn't-already-cut appears anywhere in this cave — consistent with
  `HACK_PLAN.md`'s note that Bugsy's Fire/Flying/Rock counters need to come from elsewhere on the
  approach (Route 33/Ilex Forest, or a deliberately "pulled forward" species per the open Growlithe
  suggestion).
- B2F's higher level range (20–23) versus 1F/B1F (4–9) is a large jump reflecting vanilla's
  "second half of the cave, after backtracking from Route 33" design — worth keeping in mind if
  this cave's levels get rebalanced, since B2F is effectively past-Bugsy content in vanilla
  progression even though it's the same physical dungeon.
