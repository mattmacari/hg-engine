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

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 (1F) / 15 (B2F) | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table

### 1F (walk, rate 5)

| Slot | % | Level | Morning/Day/Night |
|---|---|---|---|
| 1 | 20 | 5 | Zubat |
| 2 | 20 | 6 | Zubat |
| 3 | 10 | 5 | Zubat |
| 4 | 10 | 6 | Zubat |
| 5 | 10 | 7 | Zubat |
| 6 | 10 | 7 | Zubat |
| 7 | 5 | 6 | Slowpoke |
| 8 | 5 | 6 | Slowpoke |
| 9 | 4 | 8 | Zubat |
| 10 | 4 | 8 | Slowpoke |
| 11 | 1 | 8 | Zubat |
| 12 | 1 | 8 | Slowpoke |

No morning/day/night variation on either floor.

### B2F (walk, rate 15)

| Slot | % | Level | Morning/Day/Night |
|---|---|---|---|
| 1 | 20 | 21 | Zubat |
| 2 | 20 | 23 | Zubat |
| 3 | 10 | 21 | Zubat |
| 4 | 10 | 23 | Zubat |
| 5 | 10 | 19 | Zubat |
| 6 | 10 | 19 | Zubat |
| 7 | 5 | 21 | Slowpoke |
| 8 | 5 | 21 | Slowpoke |
| 9 | 4 | 23 | Golbat |
| 10 | 4 | 23 | Slowpoke |
| 11 | 1 | 23 | Golbat |
| 12 | 1 | 23 | Slowpoke |

## Water/rod tables

**1F surf (rate 10):** Slowpoke ×5, at declining level ranges (10–20/15–25/5–15/5–15/5–15,
60/30/5/4/1%) — this floor's surf table is 100% Slowpoke.
**B2F surf (rate 10):** Slowpoke ×2 (10–20/15–25, 60/30%), Slowbro ×3 (15–25/15–25/30, 5/4/1%).
**Both floors, old/good/super rod:** Magikarp ×3 + Goldeen ×2 (old, level 10); Magikarp + Goldeen
×4 (good, level 20); Goldeen ×2, Magikarp, Seaking, Magikarp (super, level 40) — identical to
Union Cave 1F/B1F's fishing tables.

## Rustling grass (Hoenn/Sinnoh sound species, both floors)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

Identical to Union Cave's rustling-grass pool.

## Swarm

- `landSwarm = SPECIES_ZUBAT` (both floors), `surfSwarm = SPECIES_SLOWPOKE` (both floors).
- **Inert:** neither `MAP_D26R0102` nor `MAP_D26R0103` is in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Floor(s) | Method |
|---|---|---|---|---|
| Slowbro | Water/Psychic | 349 | B2F | Surf |
| Absol | Dark | 228 | Both | Rustling grass (Hoenn) |
| Magikarp | Water | 65 | Both | Fish |
| Zubat | Poison/Flying | **not in regional dex** | Both | Walk |
| Golbat | Poison/Flying | **not in regional dex** | B2F | Walk |
| Slowpoke | Water/Psychic | 367 | Both | Walk/Surf |
| Goldeen | Water | **not in regional dex** | Both | Fish |
| Seaking | Water | **not in regional dex** | Both | Fish |
| Makuhita | Fighting | **not in regional dex** | Both | Rustling grass (Hoenn) |
| Bronzor | Steel/Psychic | **not in regional dex** | Both | Rustling grass (Sinnoh) |
| Chingling | Psychic | **not in regional dex** | Both | Rustling grass (Sinnoh) |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's tables are finalized.

## Notes

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
