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

## Encounter methods active (all three floors)

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 (1F) / 15 (B1F) / 15 (B2F) | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table

### 1F (walk, rate 10)

| Slot | % | Level | Morning/Day/Night |
|---|---|---|---|
| 1 | 20 | 6 | Geodude |
| 2 | 20 | 6 | Sandshrew |
| 3 | 10 | 6 | Geodude |
| 4 | 10 | 6 | Sandshrew |
| 5 | 10 | 5 | Zubat |
| 6 | 10 | 5 | Zubat |
| 7 | 5 | 4 | Rattata |
| 8 | 5 | 4 | Rattata |
| 9 | 4 | 7 | Zubat |
| 10 | 4 | 6 | Onix |
| 11 | 1 | 7 | Zubat |
| 12 | 1 | 6 | Onix |

No morning/day/night variation on any floor of this cave.

### B1F (walk, rate 15)

| Slot | % | Level | Morning/Day/Night |
|---|---|---|---|
| 1 | 20 | 8 | Geodude |
| 2 | 20 | 8 | Sandshrew |
| 3 | 10 | 8 | Geodude |
| 4 | 10 | 8 | Sandshrew |
| 5 | 10 | 7 | Zubat |
| 6 | 10 | 7 | Zubat |
| 7 | 5 | 8 | Onix |
| 8 | 5 | 8 | Onix |
| 9 | 4 | 9 | Zubat |
| 10 | 4 | 6 | Rattata |
| 11 | 1 | 9 | Zubat |
| 12 | 1 | 6 | Rattata |

### B2F (walk, rate 15)

| Slot | % | Level | Morning/Day/Night |
|---|---|---|---|
| 1 | 20 | 22 | Zubat |
| 2 | 20 | 22 | Raticate |
| 3 | 10 | 22 | Zubat |
| 4 | 10 | 22 | Raticate |
| 5 | 10 | 22 | Golbat |
| 6 | 10 | 22 | Golbat |
| 7 | 5 | 21 | Geodude |
| 8 | 5 | 21 | Geodude |
| 9 | 4 | 20 | Rattata |
| 10 | 4 | 23 | Onix |
| 11 | 1 | 20 | Rattata |
| 12 | 1 | 23 | Onix |

## Water/rod tables

**1F/B1F surf (rate 15):** Wooper (10–20, 60%), Quagsire ×4 (15–25/10–20/10–20/10–20, 30/5/4/1%).
**1F/B1F old/good/super rod:** Magikarp ×3 + Goldeen ×2 (old, level 10); Magikarp + Goldeen ×4
(good, level 20); Goldeen ×2, Magikarp, Seaking, Magikarp (super, level 40).

**B2F surf (rate 15):** Tentacool (10–20, 60%), Quagsire (15–25, 30%), Tentacruel ×3
(15–25/15–25/15–25, 5/4/1%). **B2F rod:** Magikarp ×3 + Krabby ×2 (old, level 10); Magikarp +
Krabby ×3 + Corsola (good, level 20); Krabby ×3, Corsola, Kingler (super, level 40) — B2F is the
one floor that swaps to the Krabby/Corsola/Kingler fishing line instead of Goldeen/Seaking.

## Rustling grass (Hoenn/Sinnoh sound species, all three floors)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

## Swarm

- `landSwarm = SPECIES_GEODUDE` (1F/B1F) / `SPECIES_ZUBAT` (B2F); `surfSwarm = SPECIES_WOOPER`
  (1F/B1F) / `SPECIES_TENTACOOL` (B2F).
- **Inert:** none of `MAP_D25R0101`/`MAP_D25R0102`/`MAP_D25R0103` are in `sSwarmMapLUT`
  (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Floor(s) | Method |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | 1F/B1F/B2F | Walk |
| Sandshrew | Ground | 41 | 1F/B1F | Walk |
| Onix | Rock/Ground | 55 | 1F/B1F/B2F | Walk |
| Wooper | Water/Ground | 49 | 1F/B1F | Surf |
| Quagsire | Water/Ground | 50 | 1F/B1F/B2F | Surf |
| Corsola | Water/Rock | 129 | B2F | Fish |
| Absol | Dark | 228 | All | Rustling grass (Hoenn) |
| Zubat | Poison/Flying | **not in regional dex** | 1F/B1F/B2F | Walk |
| Golbat | Poison/Flying | **not in regional dex** | B2F | Walk |
| Rattata | Normal | **not in regional dex** | 1F/B1F/B2F | Walk |
| Raticate | Normal | **not in regional dex** | B2F | Walk |
| Magikarp | Water | 65 | All | Fish |
| Goldeen | Water | **not in regional dex** | 1F/B1F | Fish |
| Seaking | Water | **not in regional dex** | 1F/B1F | Fish |
| Tentacool | Water/Poison | **not in regional dex** | B2F | Surf |
| Tentacruel | Water/Poison | **not in regional dex** | B2F | Surf |
| Krabby | Water | **not in regional dex** | B2F | Fish |
| Kingler | Water | **not in regional dex** | B2F | Fish |
| Makuhita | Fighting | **not in regional dex** | All | Rustling grass (Hoenn) |
| Bronzor | Steel/Psychic | **not in regional dex** | All | Rustling grass (Sinnoh) |
| Chingling | Psychic | **not in regional dex** | All | Rustling grass (Sinnoh) |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this area's tables are finalized.

## Notes

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
