# Ice Path (1F / B1F / B2F / B3F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers all four floors in one doc; they share an identical species layout, with levels
shifting by one between the upper and lower floors.

## Header facts

- **ENCDATA constants:**
  - `ENCDATA_D39R0101_ICE_PATH_1F` (`data/Encounters.c:6009`)
  - `ENCDATA_D39R0102_ICE_PATH_B1F` (`data/Encounters.c:6109`)
  - `ENCDATA_D39R0103_ICE_PATH_B2F` (`data/Encounters.c:6209`)
  - `ENCDATA_D39R0104_ICE_PATH_B3F` (`data/Encounters.c:6309`)
- **Map constants:** `MAP_D39R0101` (`include/constants/maps.h:124`), `MAP_D39R0102` (`:241`),
  `MAP_D39R0103` (`:242`), `MAP_D39R0104` (`:243`)
- **Connects:** Route 44 (west) ↔ Blackthorn City (east).
- **Leads toward:** Clair — the last area before Blackthorn.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Clair row needs Ice/Dragon/Fairy counters. This cave is
  the corridor's main Ice source.


## 1F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

### Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 21 | Swinub | Swinub | Swinub |
| 2 | 20 | 22 | Sneasel | Sneasel | Sneasel |
| 3 | 10 | 21 | Swinub | Swinub | Swinub |
| 4 | 10 | 22 | Sneasel | Sneasel | Sneasel |
| 5 | 10 | 22 | Snorunt | Snorunt | Snorunt |
| 6 | 10 | 22 | Snorunt | Snorunt | Snorunt |
| 7 | 5 | 23 | Swinub | Swinub | Swinub |
| 8 | 5 | 23 | Swinub | Swinub | Swinub |
| 9 | 4 | 22 | Snorunt | Jynx | Snorunt |
| 10 | 4 | 22 | Jynx | Jynx | Jynx |
| 11 | 1 | 22 | Snorunt | Jynx | Snorunt |
| 12 | 1 | 22 | Jynx | Jynx | Jynx |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SWINUB`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Swinub | Ice/Ground | 148 | Walk, Swarm (land) | Morning/Day/Night |
| Sneasel | Dark/Ice | 166 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Snorunt | Ice | 230 | Walk | Morning/Day/Night |
| Jynx | Ice/Psychic | 354 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B1F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

### Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 21 | Swinub | Swinub | Swinub |
| 2 | 20 | 22 | Sneasel | Sneasel | Sneasel |
| 3 | 10 | 21 | Swinub | Swinub | Swinub |
| 4 | 10 | 22 | Sneasel | Sneasel | Sneasel |
| 5 | 10 | 22 | Snorunt | Snorunt | Snorunt |
| 6 | 10 | 22 | Snorunt | Snorunt | Snorunt |
| 7 | 5 | 23 | Swinub | Swinub | Swinub |
| 8 | 5 | 23 | Swinub | Swinub | Swinub |
| 9 | 4 | 22 | Snorunt | Jynx | Snorunt |
| 10 | 4 | 22 | Jynx | Jynx | Jynx |
| 11 | 1 | 22 | Snorunt | Jynx | Snorunt |
| 12 | 1 | 22 | Jynx | Jynx | Jynx |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SWINUB`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Swinub | Ice/Ground | 148 | Walk, Swarm (land) | Morning/Day/Night |
| Sneasel | Dark/Ice | 166 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Snorunt | Ice | 230 | Walk | Morning/Day/Night |
| Jynx | Ice/Psychic | 354 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B2F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

### Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 22 | Swinub | Swinub | Swinub |
| 2 | 20 | 23 | Sneasel | Sneasel | Sneasel |
| 3 | 10 | 22 | Swinub | Swinub | Swinub |
| 4 | 10 | 23 | Sneasel | Sneasel | Sneasel |
| 5 | 10 | 23 | Snorunt | Snorunt | Snorunt |
| 6 | 10 | 23 | Snorunt | Snorunt | Snorunt |
| 7 | 5 | 24 | Swinub | Swinub | Swinub |
| 8 | 5 | 24 | Swinub | Swinub | Swinub |
| 9 | 4 | 23 | Snorunt | Jynx | Snorunt |
| 10 | 4 | 23 | Jynx | Jynx | Jynx |
| 11 | 1 | 23 | Snorunt | Jynx | Snorunt |
| 12 | 1 | 23 | Jynx | Jynx | Jynx |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SWINUB`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Swinub | Ice/Ground | 148 | Walk, Swarm (land) | Morning/Day/Night |
| Sneasel | Dark/Ice | 166 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Snorunt | Ice | 230 | Walk | Morning/Day/Night |
| Jynx | Ice/Psychic | 354 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B3F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

### Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 22 | Swinub | Swinub | Swinub |
| 2 | 20 | 23 | Sneasel | Sneasel | Sneasel |
| 3 | 10 | 22 | Swinub | Swinub | Swinub |
| 4 | 10 | 23 | Sneasel | Sneasel | Sneasel |
| 5 | 10 | 23 | Snorunt | Snorunt | Snorunt |
| 6 | 10 | 23 | Snorunt | Snorunt | Snorunt |
| 7 | 5 | 24 | Swinub | Swinub | Swinub |
| 8 | 5 | 24 | Swinub | Swinub | Swinub |
| 9 | 4 | 23 | Snorunt | Jynx | Snorunt |
| 10 | 4 | 23 | Jynx | Jynx | Jynx |
| 11 | 1 | 23 | Snorunt | Jynx | Snorunt |
| 12 | 1 | 23 | Jynx | Jynx | Jynx |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SWINUB`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Swinub | Ice/Ground | 148 | Walk, Swarm (land) | Morning/Day/Night |
| Sneasel | Dark/Ice | 166 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Snorunt | Ice | 230 | Walk | Morning/Day/Night |
| Jynx | Ice/Psychic | 354 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


Dex numbers as of `data/RegionalDex.c` with 374 entries — re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Zubat/Golbat replaced with Ice types** on all four floors:
  - Zubat (25% morning/night, 20% by day) → **Snorunt** (#230).
  - Golbat (slots 2/4, 30%) → **Sneasel** (#166).
  - Both are dex-tracked; Sneasel previously spawned only on Mt. Silver/Route 28.
  - These replace this session's usual Woobat stand-in because Ice Path is the corridor's ice
    biome, and both add to Clair's Ice counter-access alongside Swinub and Jynx.
- **Left as-is:** dex-less rustling-grass species (post-game only).
