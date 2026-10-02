# Slowpoke Well (1F / B2F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers both existing floors in one doc since they share the same species pool (see Notes on
the missing "B1F").

## Header facts

- **ENCDATA constants:** `ENCDATA_D26R0102_SLOWPOKE_WELL_1F` (`data/Encounters.c:1809`),
  `ENCDATA_D26R0103_SLOWPOKE_WELL_B2F` (`data/Encounters.c:1909`)
- **Map constants:** `MAP_D26R0102` (`include/constants/maps.h:181`),
  `MAP_D26R0103` (`include/constants/maps.h:185`)
- **Connects:** inside Azalea Town (down the well entrance) — optional/story-flagged content (Team
  Rocket occupies it in vanilla until the post-Bugsy story beat resolves it).
- **Leads toward:** Bugsy (Azalea Town) — optional side content, not on the critical gym path.
- **Biome Map tie-in:** not named directly in `HACK_PLAN.md`'s Bugsy row (which centers on Ilex
  Forest bug variety and the Fire/Flying/Rock counter-access note). This well's own identity is
  entirely Slowpoke-branded by name and vanilla lore — see Notes for why that's a live tension
  with the current regional dex curation.

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
| 1 | 20 | 5 | Woobat | Woobat | Woobat |
| 2 | 20 | 6 | Woobat | Woobat | Woobat |
| 3 | 10 | 5 | Woobat | Woobat | Woobat |
| 4 | 10 | 6 | Woobat | Woobat | Woobat |
| 5 | 10 | 7 | Woobat | Woobat | Woobat |
| 6 | 10 | 7 | Woobat | Woobat | Woobat |
| 7 | 5 | 6 | Slowpoke | Slowpoke | Slowpoke |
| 8 | 5 | 6 | Slowpoke | Slowpoke | Slowpoke |
| 9 | 4 | 8 | Woobat | Woobat | Woobat |
| 10 | 4 | 8 | Slowpoke | Slowpoke | Slowpoke |
| 11 | 1 | 8 | Woobat | Woobat | Woobat |
| 12 | 1 | 8 | Slowpoke | Slowpoke | Slowpoke |

### Water/rod tables

**Surf (rate 10):** Slowpoke (10–20), Slowpoke (15–25), Slowpoke (5–15), Slowpoke (5–15), Slowpoke (5–15).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Wooper (10), Wooper (10).
**Good Rod (rate 50):** Magikarp (20), Wooper (20), Wooper (20), Wooper (20), Wooper (20).
**Super Rod (rate 75):** Wooper (40), Wooper (40), Magikarp (40), Quagsire (40), Magikarp (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_WOOBAT`, `surfSwarm = SPECIES_SLOWPOKE`, `nightFish = SPECIES_WOOPER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Wooper | Water/Ground | 49 | Fish, Fish (night) | — |
| Quagsire | Water/Ground | 50 | Fish | — |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk, Swarm (land) | Morning/Day/Night |
| Slowpoke | Water/Psychic | 367 | Walk, Surf, Swarm (surf) | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


## B2F

### Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 15 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Land encounter table (walk, rate 15)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 21 | Woobat | Woobat | Woobat |
| 2 | 20 | 23 | Woobat | Woobat | Woobat |
| 3 | 10 | 21 | Woobat | Woobat | Woobat |
| 4 | 10 | 23 | Woobat | Woobat | Woobat |
| 5 | 10 | 19 | Woobat | Woobat | Woobat |
| 6 | 10 | 19 | Woobat | Woobat | Woobat |
| 7 | 5 | 21 | Slowpoke | Slowpoke | Slowpoke |
| 8 | 5 | 21 | Slowpoke | Slowpoke | Slowpoke |
| 9 | 4 | 23 | Swoobat | Swoobat | Swoobat |
| 10 | 4 | 23 | Slowpoke | Slowpoke | Slowpoke |
| 11 | 1 | 23 | Swoobat | Swoobat | Swoobat |
| 12 | 1 | 23 | Slowpoke | Slowpoke | Slowpoke |

### Water/rod tables

**Surf (rate 10):** Slowpoke (10–20), Slowpoke (15–25), Slowbro (15–25), Slowbro (15–25), Slowbro (30).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Wooper (10), Wooper (10).
**Good Rod (rate 50):** Magikarp (20), Wooper (20), Wooper (20), Wooper (20), Wooper (20).
**Super Rod (rate 75):** Wooper (40), Wooper (40), Magikarp (40), Quagsire (40), Magikarp (40).

### Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

### Swarm

- `landSwarm = SPECIES_WOOBAT`, `surfSwarm = SPECIES_SLOWPOKE`, `nightFish = SPECIES_WOOPER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

### Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Wooper | Water/Ground | 49 | Fish, Fish (night) | — |
| Quagsire | Water/Ground | 50 | Fish | — |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk, Swarm (land) | Morning/Day/Night |
| Swoobat | Psychic/Flying | 277 | Walk | Morning/Day/Night |
| Slowbro | Water/Psychic | 349 | Surf | — |
| Slowpoke | Water/Psychic | 367 | Walk, Surf, Swarm (surf) | Morning/Day/Night |
| Bronzor | Steel/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Makuhita | Fighting | **not in dex** | Rustling grass (Hoenn) | — |


Dex numbers as of `data/RegionalDex.c` with 377 entries — re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** Zubat/Golbat →
  **Woobat/Swoobat** (#276/#277), including the inert land swarm. Goldeen/Seaking →
  **Wooper/Quagsire**, matching Union Cave and Dark Cave. Earlier notes below that describe these species as dex-less or intentionally kept are superseded.
- **Resolved — Slowpoke's dex-cut-while-Slowbro-was-kept was a curation oversight, now fixed.**
  Flipped `keep` to `Yes` for `SPECIES_SLOWPOKE` in `data/generated/species_dex_meta.csv` and added
  `[SPECIES_SLOWPOKE] = 367` to `data/RegionalDex.c` (appended per the existing file's append-order
  convention, same as every other post-baseline addition — no reordering next to Slowbro's #349).
  The species summary table above is stale on this point; Slowpoke is now regional dex #367.
- Golbat/Goldeen/Seaking dex-less here follows the same routine convention as Union Cave (this well
  reuses Union Cave's exact fishing table and rustling-grass pool).
- **Type-coverage relevance (Pillar 3, Bugsy):** nothing here contributes Fire/Flying/Rock — this
  area is optional/story-gated side content, not a load-bearing part of the audit.
- **"B1F" doesn't exist as a separate encounter area:** `MAP_D26R0101` is a valid map constant
  (`include/constants/maps.h:118`) but has no `ENCDATA_*` entry in `data/Encounters.c` — it's
  presumably a fixed-encounter/cutscene-only map (the Team Rocket confrontation floor) with no wild
  table, not a gap in this doc.
