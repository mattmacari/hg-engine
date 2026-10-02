# Mt. Mortar (1F waterfall room / central room / room above waterfall / B1F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers all four rooms in one doc; each room keeps its own tables below.

## Header facts

- **ENCDATA constants:**
  - `ENCDATA_D38R0101_MT_MORTAR_WATERFALL_ROOM` (`data/Encounters.c:5309`)
  - `ENCDATA_D38R0102_MT_MORTAR_CENTRAL_ROOM` (`data/Encounters.c:5409`)
  - `ENCDATA_D38R0103_MT_MORTAR_ROOM_ABOVE_WATERFALL` (`data/Encounters.c:5509`)
  - `ENCDATA_D38R0104_MT_MORTAR_B1F` (`data/Encounters.c:5609`)
- **Map constants:** `MAP_D38R0101` (`include/constants/maps.h:123`), `MAP_D38R0102` (`:254`),
  `MAP_D38R0103` (`:255`), `MAP_D38R0104` (`:256`)
- **Connects:** entrances along Route 42.
- **Leads toward:** Pryce — side cave on the Route 42 leg. The room above the waterfall (Lv28–32)
  is gated behind Waterfall and plays as later/optional content. The Karate King's gift Tyrogue is
  here, so wild Tyrogue was deliberately **not** used as a replacement.
- **Biome Map tie-in:** Rock/Fighting cave — Machop/Machoke and Geodude/Graveler give Pryce's
  Fighting and Rock counters.


## 1F — waterfall room

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 13 | Woobat | Woobat | Woobat |
| 2 | 20 | 15 | Woobat | Woobat | Woobat |
| 3 | 10 | 13 | Woobat | Woobat | Woobat |
| 4 | 10 | 15 | Woobat | Woobat | Woobat |
| 5 | 10 | 14 | Machop | Machop | Machop |
| 6 | 10 | 14 | Machop | Machop | Machop |
| 7 | 5 | 14 | Drilbur | Drilbur | Drilbur |
| 8 | 5 | 14 | Drilbur | Drilbur | Drilbur |
| 9 | 4 | 14 | Geodude | Geodude | Geodude |
| 10 | 4 | 16 | Drilbur | Drilbur | Drilbur |
| 11 | 1 | 14 | Geodude | Geodude | Geodude |
| 12 | 1 | 15 | Marill | Marill | Marill |

### Water/rod tables

**Surf (rate 10):** Marill (15–25), Surskit (10–20), Azumarill (15–25), Masquerain (15–25), Azumarill (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Marill (10), Surskit (10).
**Good Rod (rate 50):** Magikarp (20), Marill (20), Surskit (20), Marill (20), Surskit (20).
**Super Rod (rate 75):** Marill (40), Surskit (40), Magikarp (40), Azumarill (40), Feebas (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_MARILL`, `surfSwarm = SPECIES_SURSKIT`, `nightFish = SPECIES_MARILL`, `fishSwarm = SPECIES_MAGIKARP`.
- **Active (land only):** `MAP_D38R0101` is in `sSwarmMapLUT` (`src/swarms.c:29`, `SWARM_GRASS`) — the Marill land swarm fires here; surf/fish swarm fields are inert.

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Marill | Water/Fairy | 102 | Walk, Surf, Fish, Swarm (land), Fish (night) | Morning/Day/Night |
| Azumarill | Water/Fairy | 103 | Surf, Fish | — |
| Machop | Fighting | 106 | Walk | Morning/Day/Night |
| Surskit | Bug/Water | 211 | Surf, Fish, Swarm (surf) | — |
| Masquerain | Bug/Flying | 212 | Surf | — |
| Feebas | Water | 226 | Fish | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Drilbur | Ground | 278 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## Central room

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

### Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 13 | Geodude | Geodude | Geodude |
| 2 | 20 | 13 | Machop | Machop | Machop |
| 3 | 10 | 13 | Geodude | Geodude | Geodude |
| 4 | 10 | 13 | Machop | Machop | Machop |
| 5 | 10 | 15 | Geodude | Geodude | Geodude |
| 6 | 10 | 15 | Geodude | Geodude | Geodude |
| 7 | 5 | 14 | Drilbur | Drilbur | Drilbur |
| 8 | 5 | 14 | Drilbur | Drilbur | Drilbur |
| 9 | 4 | 15 | Machop | Machop | Machop |
| 10 | 4 | 14 | Woobat | Woobat | Woobat |
| 11 | 1 | 15 | Machop | Machop | Machop |
| 12 | 1 | 14 | Woobat | Woobat | Woobat |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_GEODUDE`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk, Swarm (land) | Morning/Day/Night |
| Machop | Fighting | 106 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Drilbur | Ground | 278 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## Room above waterfall

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 31 | Graveler | Graveler | Graveler |
| 2 | 20 | 32 | Machoke | Machoke | Machoke |
| 3 | 10 | 31 | Graveler | Graveler | Graveler |
| 4 | 10 | 32 | Machoke | Machoke | Machoke |
| 5 | 10 | 31 | Geodude | Geodude | Geodude |
| 6 | 10 | 31 | Geodude | Geodude | Geodude |
| 7 | 5 | 30 | Excadrill | Excadrill | Excadrill |
| 8 | 5 | 30 | Excadrill | Excadrill | Excadrill |
| 9 | 4 | 28 | Machop | Machop | Machop |
| 10 | 4 | 30 | Swoobat | Swoobat | Swoobat |
| 11 | 1 | 28 | Machop | Machop | Machop |
| 12 | 1 | 30 | Swoobat | Swoobat | Swoobat |

### Water/rod tables

**Surf (rate 10):** Marill (15–25), Surskit (20–30), Azumarill (20–30), Masquerain (20–30), Azumarill (20–30).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Marill (10), Surskit (10).
**Good Rod (rate 50):** Magikarp (20), Marill (20), Surskit (20), Marill (20), Surskit (20).
**Super Rod (rate 75):** Marill (40), Surskit (40), Magikarp (40), Azumarill (40), Feebas (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_GRAVELER`, `surfSwarm = SPECIES_SURSKIT`, `nightFish = SPECIES_MARILL`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk | Morning/Day/Night |
| Graveler | Rock/Ground | 31 | Walk, Swarm (land) | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Marill | Water/Fairy | 102 | Surf, Fish, Fish (night) | — |
| Azumarill | Water/Fairy | 103 | Surf, Fish | — |
| Machop | Fighting | 106 | Walk | Morning/Day/Night |
| Machoke | Fighting | 107 | Walk | Morning/Day/Night |
| Surskit | Bug/Water | 211 | Surf, Fish, Swarm (surf) | — |
| Masquerain | Bug/Flying | 212 | Surf | — |
| Feebas | Water | 226 | Fish | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Excadrill | Ground/Steel | 279 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B1F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 15 | Woobat | Woobat | Woobat |
| 2 | 20 | 17 | Woobat | Woobat | Woobat |
| 3 | 10 | 15 | Woobat | Woobat | Woobat |
| 4 | 10 | 17 | Woobat | Woobat | Woobat |
| 5 | 10 | 16 | Drilbur | Drilbur | Drilbur |
| 6 | 10 | 16 | Drilbur | Drilbur | Drilbur |
| 7 | 5 | 16 | Machop | Machop | Machop |
| 8 | 5 | 16 | Machop | Machop | Machop |
| 9 | 4 | 16 | Geodude | Geodude | Geodude |
| 10 | 4 | 16 | Drilbur | Drilbur | Drilbur |
| 11 | 1 | 16 | Geodude | Geodude | Geodude |
| 12 | 1 | 16 | Drilbur | Drilbur | Drilbur |

### Water/rod tables

**Surf (rate 10):** Marill (15–25), Surskit (10–20), Azumarill (15–25), Masquerain (15–25), Azumarill (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Marill (10), Surskit (10).
**Good Rod (rate 50):** Magikarp (20), Marill (20), Surskit (20), Marill (20), Surskit (20).
**Super Rod (rate 75):** Marill (40), Surskit (40), Magikarp (40), Azumarill (40), Feebas (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_WOOBAT`, `surfSwarm = SPECIES_SURSKIT`, `nightFish = SPECIES_MARILL`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Marill | Water/Fairy | 102 | Surf, Fish, Fish (night) | — |
| Azumarill | Water/Fairy | 103 | Surf, Fish | — |
| Machop | Fighting | 106 | Walk | Morning/Day/Night |
| Surskit | Bug/Water | 211 | Surf, Fish, Swarm (surf) | — |
| Masquerain | Bug/Flying | 212 | Surf | — |
| Feebas | Water | 226 | Fish | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk, Swarm (land) | Morning/Day/Night |
| Drilbur | Ground | 278 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


Dex numbers as of `data/RegionalDex.c` with 369 entries — re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Zubat/Golbat replaced:** Zubat → **Woobat** (60% of the 1F and B1F tables, plus
  B1F's inert land swarm). Golbat (room above waterfall) → **Swoobat**. Same bat stand-in as Cliff
  Cave.
- **Resolved — Rattata/Raticate replaced:** → **Drilbur** (#278, dex-tracked but spawned nowhere).
  A Ground digger fits the cave and adds an Excadrill path to Steel. In the room above the
  waterfall, Raticate (Lv30) → **Excadrill** (#279). That's one level under Drilbur's Lv31
  evolution, in the same accepted range as other evolved wild slots.
- **Resolved — Goldeen/Seaking replaced** with the mixed Marill/Surskit pool shared with Route 42
  (see Route-42.md).
- **New flavor — Feebas:** the 1% Super Rod slot (previously Magikarp) in all three water rooms is
  now **Feebas** (#226, dex-tracked but spawned nowhere). It's a rare mountain-waterfall find,
  echoing its Mt. Coronet lore, and it's kept Mortar-only.
- Marill (1F walk slot 12 plus the active 1F land swarm) is unchanged.
- **Left as-is:** dex-less rustling-grass species (post-game only).
