# Burned Tower (1F / B1F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers both floors in one doc, following the same convention as `Sprout-Tower.md`.

## Header facts

- **ENCDATA constants:** `ENCDATA_D18R0101_BURNED_TOWER_1F` (`data/Encounters.c:2809`),
  `ENCDATA_D18R0102_BURNED_TOWER_B1F` (`data/Encounters.c:2909`)
- **Map constants:** `MAP_D18R0101` (`include/constants/maps.h:11`),
  `MAP_D18R0102` (`include/constants/maps.h:221`)
- **Connects:** Inside Ecruteak City. Optional pre-gym content in vanilla HGSS story flow (1F is
  visited as part of the legendary-beasts cutscene before Morty; B1F access typically needs Rock
  Smash) — not required to challenge Morty, same relationship Sprout Tower has to Falkner.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Morty row cites "Burned Tower / old-town lore" as already
  a strong Ghost biome fit — that used to be about the location's story/flavor role only (site of
  the Ho-Oh/legendary-beasts event), since the wild table was plain Rattata/Koffing/Zubat filler
  with no Ghost-type presence at all. **Resolved** — the wild table now actually delivers on that
  Ghost biome too, see Notes.

## Encounter methods active

Identical for both floors — no water/rod methods, walk only, low indoor rate.

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table — 1F (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 13 | Ekans | Ekans | **Gastly** |
| 2 | 20 | 14 | Grimer | Grimer | Grimer |
| 3 | 10 | 13 | Ekans | Ekans | **Gastly** |
| 4 | 10 | 14 | Grimer | Grimer | Grimer |
| 5 | 10 | 15 | Ekans | Ekans | **Gastly** |
| 6 | 10 | 15 | Ekans | Ekans | **Gastly** |
| 7 | 5 | 14 | Haunter | Haunter | Haunter |
| 8 | 5 | 14 | Haunter | Haunter | Haunter |
| 9 | 4 | 16 | Grimer | Grimer | Grimer |
| 10 | 4 | 15 | Muk | Muk | Muk |
| 11 | 1 | 16 | Grimer | Grimer | Grimer |
| 12 | 1 | 15 | Muk | Muk | Muk |

Night flips the four Ekans slots (50% of the table) to Gastly — mirrors Sprout Tower's own
night-time Sentret→Gastly pattern exactly (see Notes).

## Land encounter table — B1F (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 14 | Ekans | Ekans | Ekans |
| 2 | 20 | 14 | Grimer | Grimer | Grimer |
| 3 | 10 | 14 | Ekans | Ekans | Ekans |
| 4 | 10 | 14 | Grimer | Grimer | Grimer |
| 5 | 10 | 16 | Grimer | Grimer | Grimer |
| 6 | 10 | 16 | Grimer | Grimer | Grimer |
| 7 | 5 | 16 | Ekans | Magmar | Ekans |
| 8 | 5 | 16 | Ekans | Magmar | Ekans |
| 9 | 4 | 15 | Haunter | Haunter | Haunter |
| 10 | 4 | 14 | Magmar | Ekans | Magmar |
| 11 | 1 | 15 | Haunter | Haunter | Haunter |
| 12 | 1 | 14 | Magmar | Ekans | Magmar |

B1F swaps two of the day-time Ekans slots (7/8) for Magmar — the only time-of-day variance on
either floor, unchanged from before this pass (Magmar's placement was already correct, only the
species around it were dex-less).

## Rustling grass (Hoenn/Sinnoh sound species) — both floors

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Zigzagoon | Spinda |
| Sinnoh | Chatot | Meditite |

Same rustling-grass pool as Sprout Tower.

## Swarm

- Both floors: `landSwarm = SPECIES_EKANS`.
- **Inert:** neither `MAP_D18R0101` nor `MAP_D18R0102` is in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magmar | Fire | 114 | Walk (B1F only) | Day (slots 7/8), Morning/Night (slot 10/12) |
| Gastly | Ghost/Poison | 51 | Walk (1F only) | Night |
| Haunter | Ghost/Poison | 52 | Walk | Morning/Day/Night |
| Ekans | Poison | 43 | Walk, Swarm (land, inert) | Morning/Day/Night (1F day/morning only) |
| Grimer | Poison | 88 | Walk | Morning/Day/Night |
| Muk | Poison | 89 | Walk (1F only) | Morning/Day/Night |
| Zigzagoon | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Spinda | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Chatot | Normal/Flying | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Meditite | Fighting/Psychic | **not in regional dex, sheet decision still `Maybe`** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- **Resolved — Rattata/Raticate/Koffing/Zubat replaced across both floors.** These four made up
  100% of 1F and ~90-95% of B1F while sitting dex-less (both halves of the Rattata/Raticate and
  Koffing/Weezing lines are cut from `data/RegionalDex.c`, and so is the whole Zubat/Golbat line —
  confirmed no oversight). Replaced with **Ekans**, **Grimer**, **Muk**, **Haunter**, and (1F night
  only) **Gastly** — all five already regional-dex-tracked (#43/#88/#89/#52/#51) and, apart from
  Gastly/Haunter's use at Sprout Tower and Bell Tower, not spawning anywhere else in the build.
- **The Gastly night-flip on 1F isn't a new idea — it copies a pattern this hack already
  established.** `ENCDATA_D15R0102_SPROUT_TOWER_2F`/`3F` swap their common filler (Sentret) for
  Gastly at night; Bell Tower (post-game) runs Gastly across most floors. Burned Tower having zero
  Ghost-type presence despite being the other pre-game "tower," while the doc's own Biome Map note
  called out its strong Ghost lore, looked like an oversight rather than a deliberate cut — this
  closes that gap using the same convention rather than inventing a new one.
- B1F runs Haunter (not Gastly) as its base ghost presence instead of a night-only flip — B1F is
  Rock-Smash-gated bonus content already, so it can afford to read as tougher than 1F without
  needing its own time-of-day split.
- Magmar (B1F only) is untouched — it was already the one dex-tracked species on either floor
  (#114) and already had a documented thematic reason (fire-damage lore); only the species around
  it were dex-less.
- **Meditite is the same open `keep = Maybe` decision flagged in `Sprout-Tower.md`** — not a
  routine cut, worth resolving as part of the broader curation-sheet cleanup rather than here.
