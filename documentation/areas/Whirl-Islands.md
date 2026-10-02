# Whirl Islands (1F / B1F / B2F / B3F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers the four floors with live encounter tables in one doc. The `ENCDATA_UNUSED_045/047/049/050`
entries between them are unused placeholders and aren't documented.

## Header facts

- **ENCDATA constants:**
  - `ENCDATA_D40R0101_WHIRL_ISLANDS_1F` (`data/Encounters.c:4309`)
  - `ENCDATA_D40R0102_WHIRL_ISLANDS_B1F` (`data/Encounters.c:4409`)
  - `ENCDATA_D40R0104_WHIRL_ISLANDS_B2F` (`data/Encounters.c:4609`)
  - `ENCDATA_D40R0106_WHIRL_ISLANDS_B3F_LEDGE_OVERLOOKING_LUGIA_ROOM` (`data/Encounters.c:4809`)
- **Map constants:** `MAP_D40R0101` (`include/constants/maps.h:125`), `MAP_D40R0102` (`:246`),
  `MAP_D40R0104` (`:247`), `MAP_D40R0106` (`:490`)
- **Connects:** the Route 41 sea between Olivine and Cianwood. Entry needs Whirlpool.
- **Leads toward:** optional side area. Lance hands over Whirlpool after the Rocket Hideout, before
  Pryce's gym opens, so it falls in the Pryce/Clair window. The Lugia encounter is scripted (and
  needs the Silver Wing), not part of these tables.

## 1F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 22 | Shellder | Shellder | Shellder |
| 2 | 20 | 23 | Woobat | Woobat | Woobat |
| 3 | 10 | 22 | Shellder | Shellder | Shellder |
| 4 | 10 | 23 | Woobat | Woobat | Woobat |
| 5 | 10 | 24 | Spheal | Spheal | Spheal |
| 6 | 10 | 24 | Spheal | Spheal | Spheal |
| 7 | 5 | 22 | Seel | Seel | Seel |
| 8 | 5 | 22 | Seel | Seel | Seel |
| 9 | 4 | 23 | Swoobat | Swoobat | Swoobat |
| 10 | 4 | 24 | Seel | Seel | Seel |
| 11 | 1 | 23 | Swoobat | Swoobat | Swoobat |
| 12 | 1 | 24 | Seel | Seel | Seel |

### Water/rod tables

**Surf (rate 10):** Staryu (15–25), Horsea (10–20), Starmie (15–25), Starmie (15–25), Starmie (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Shellder (10), Shellder (10).
**Good Rod (rate 50):** Magikarp (20), Shellder (20), Shellder (20), Horsea (20), Shellder (20).
**Super Rod (rate 75):** Shellder (40), Horsea (40), Cloyster (40), Seadra (40), Cloyster (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SHELLDER`, `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_HORSEA`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Staryu | Water | 125 | Surf, Swarm (surf) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water | 127 | Walk, Fish, Swarm (land) | Morning/Day/Night |
| Cloyster | Water/Ice | 128 | Fish | — |
| Seel | Water | 134 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Spheal | Ice/Water | 232 | Walk | Morning/Day/Night |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Horsea | Water | 370 | Surf, Fish, Fish (night) | — |
| Seadra | Water | 371 | Fish | — |
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
| 1 | 20 | 22 | Shellder | Shellder | Shellder |
| 2 | 20 | 23 | Woobat | Woobat | Woobat |
| 3 | 10 | 22 | Shellder | Shellder | Shellder |
| 4 | 10 | 23 | Woobat | Woobat | Woobat |
| 5 | 10 | 24 | Spheal | Spheal | Spheal |
| 6 | 10 | 24 | Spheal | Spheal | Spheal |
| 7 | 5 | 22 | Seel | Seel | Seel |
| 8 | 5 | 22 | Seel | Seel | Seel |
| 9 | 4 | 23 | Swoobat | Swoobat | Swoobat |
| 10 | 4 | 24 | Seel | Seel | Seel |
| 11 | 1 | 23 | Swoobat | Swoobat | Swoobat |
| 12 | 1 | 24 | Seel | Seel | Seel |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SHELLDER`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Shellder | Water | 127 | Walk, Swarm (land) | Morning/Day/Night |
| Seel | Water | 134 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Spheal | Ice/Water | 232 | Walk | Morning/Day/Night |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B2F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 22 | Shellder | Shellder | Shellder |
| 2 | 20 | 23 | Woobat | Woobat | Woobat |
| 3 | 10 | 22 | Shellder | Shellder | Shellder |
| 4 | 10 | 23 | Woobat | Woobat | Woobat |
| 5 | 10 | 24 | Spheal | Spheal | Spheal |
| 6 | 10 | 24 | Spheal | Spheal | Spheal |
| 7 | 5 | 22 | Seel | Seel | Seel |
| 8 | 5 | 22 | Seel | Seel | Seel |
| 9 | 4 | 23 | Swoobat | Swoobat | Swoobat |
| 10 | 4 | 24 | Seel | Seel | Seel |
| 11 | 1 | 23 | Swoobat | Swoobat | Swoobat |
| 12 | 1 | 24 | Seel | Seel | Seel |

### Water/rod tables

**Surf (rate 10):** Horsea (15–25), Starmie (15–25), Seadra (15–25), Seadra (15–25), Seadra (30).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Shellder (10), Shellder (10).
**Good Rod (rate 50):** Magikarp (20), Shellder (20), Shellder (20), Horsea (20), Shellder (20).
**Super Rod (rate 75):** Shellder (40), Horsea (40), Cloyster (40), Seadra (40), Cloyster (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SHELLDER`, `surfSwarm = SPECIES_HORSEA`, `nightFish = SPECIES_HORSEA`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water | 127 | Walk, Fish, Swarm (land) | Morning/Day/Night |
| Cloyster | Water/Ice | 128 | Fish | — |
| Seel | Water | 134 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Spheal | Ice/Water | 232 | Walk | Morning/Day/Night |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Horsea | Water | 370 | Surf, Fish, Swarm (surf), Fish (night) | — |
| Seadra | Water | 371 | Surf, Fish | — |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B3F (ledge overlooking the Lugia room)

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
| 1 | 20 | 23 | Shellder | Shellder | Shellder |
| 2 | 20 | 24 | Woobat | Woobat | Woobat |
| 3 | 10 | 23 | Shellder | Shellder | Shellder |
| 4 | 10 | 24 | Woobat | Woobat | Woobat |
| 5 | 10 | 25 | Spheal | Spheal | Spheal |
| 6 | 10 | 25 | Spheal | Spheal | Spheal |
| 7 | 5 | 23 | Seel | Seel | Seel |
| 8 | 5 | 23 | Seel | Seel | Seel |
| 9 | 4 | 24 | Swoobat | Swoobat | Swoobat |
| 10 | 4 | 25 | Seel | Seel | Seel |
| 11 | 1 | 24 | Swoobat | Swoobat | Swoobat |
| 12 | 1 | 25 | Seel | Seel | Seel |

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_SHELLDER`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Shellder | Water | 127 | Walk, Swarm (land) | Morning/Day/Night |
| Seel | Water | 134 | Walk | Morning/Day/Night |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Spheal | Ice/Water | 232 | Walk | Morning/Day/Night |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


Dex numbers as of `data/RegionalDex.c` with 377 entries — re-`grep` if the dex is renumbered.

## Notes

- **Resolved — dex-less species replaced (Whirl Islands pass, after the early-game cleanup):**
  - Walking Krabby (slots 1/3/5/6, 50% of each floor) is split for variety: slots 1/3 → **Shellder**
    (the Krabby → Shellder precedent from Cianwood and Cliff Cave), slots 5/6 → **Spheal** (#232,
    dex-tracked but previously Safari Zone-only; an icy sea-cave fit next to Seel). The inert land
    swarm → Shellder.
  - Zubat/Golbat → **Woobat/Swoobat**, the cave-bat stand-in used across Johto.
  - Water: Tentacool/Tentacruel → **Staryu/Starmie** and Krabby/Kingler (rods) → **Shellder/
    Cloyster** — the Route 40/41/Cianwood sea mapping, which this cave sits in the middle of.
- Horsea/Seadra (surf, rods, night fish, B2F surf swarm) were already here in vanilla. They're now
  dex-tracked (#370/#371, added in the Clair pass), so this is a second, canon Horsea source
  alongside Route 44's rods.
- **Left as-is:** dex-less rustling-grass species (post-game only).
