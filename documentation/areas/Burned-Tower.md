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
  a strong Ghost biome fit — that's about the location's story/flavor role (site of the
  Ho-Oh/legendary-beasts event, thematically tied to the Brass Tower burning), not its wild
  encounter table, which is plain Rattata/Koffing/Zubat filler with no Ghost- or Dark-type
  presence. No wild-encounter changes needed here; the Dark-coverage fix lives on Route 36.

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

## Land encounter table — 1F (walk, rate 10) — identical morning/day/night

| Slot | % | Level | Species |
|---|---|---|---|
| 1 | 20 | 13 | Rattata |
| 2 | 20 | 14 | Koffing |
| 3 | 10 | 13 | Rattata |
| 4 | 10 | 14 | Koffing |
| 5 | 10 | 15 | Rattata |
| 6 | 10 | 15 | Rattata |
| 7 | 5 | 14 | Zubat |
| 8 | 5 | 14 | Zubat |
| 9 | 4 | 16 | Koffing |
| 10 | 4 | 15 | Raticate |
| 11 | 1 | 16 | Koffing |
| 12 | 1 | 15 | Raticate |

## Land encounter table — B1F (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 14 | Rattata | Rattata | Rattata |
| 2 | 20 | 14 | Koffing | Koffing | Koffing |
| 3 | 10 | 14 | Rattata | Rattata | Rattata |
| 4 | 10 | 14 | Koffing | Koffing | Koffing |
| 5 | 10 | 16 | Koffing | Koffing | Koffing |
| 6 | 10 | 16 | Koffing | Koffing | Koffing |
| 7 | 5 | 16 | Rattata | Magmar | Rattata |
| 8 | 5 | 16 | Rattata | Magmar | Rattata |
| 9 | 4 | 15 | Zubat | Zubat | Zubat |
| 10 | 4 | 14 | Magmar | Rattata | Magmar |
| 11 | 1 | 15 | Zubat | Zubat | Zubat |
| 12 | 1 | 14 | Magmar | Rattata | Magmar |

B1F swaps two of the day-time Rattata slots (7/8) for Magmar — the only time-of-day variance on
either floor.

## Rustling grass (Hoenn/Sinnoh sound species) — both floors

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Zigzagoon | Spinda |
| Sinnoh | Chatot | Meditite |

Same rustling-grass pool as Sprout Tower.

## Swarm

- Both floors: `landSwarm = SPECIES_RATTATA`.
- **Inert:** neither `MAP_D18R0101` nor `MAP_D18R0102` is in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magmar | Fire | 114 | Walk (B1F only) | Day (slots 7/8), Morning/Night (slot 10/12) |
| Rattata | Normal | **not in regional dex** | Walk, Swarm (land, inert) | Morning/Day/Night |
| Raticate | Normal | **not in regional dex** | Walk (1F only) | Morning/Day/Night |
| Koffing | Poison | **not in regional dex** | Walk | Morning/Day/Night |
| Zubat | Poison/Flying | **not in regional dex** | Walk | Morning/Day/Night |
| Zigzagoon | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Spinda | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Chatot | Normal/Flying | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Meditite | Fighting/Psychic | **not in regional dex, sheet decision still `Maybe`** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- Rattata/Raticate/Koffing/Zubat dex-less here is the same routine curation-sheet cut (`keep =
  No`) seen throughout every other approach doc so far — no evolution-mismatch case like Slowpoke
  was, since both halves of the Rattata/Raticate and Koffing/Weezing lines are cut consistently
  (checked `data/RegionalDex.c` for `GOLBAT`/`WEEZING`/`RATICATE` too — all absent, no oversight).
- Magmar (B1F only) is the one dex-tracked species on either floor (#114) — thematically fits the
  "Burned" Tower's fire-damage lore even though it's Fire, not Ghost/Dark.
- **Meditite is the same open `keep = Maybe` decision flagged in `Sprout-Tower.md`** — not a
  routine cut, worth resolving as part of the broader curation-sheet cleanup rather than here.
- No Ghost- or Dark-type wild encounters on either floor despite the tower's Ghost-adjacent story
  role — consistent with this doc's Biome Map note above: the location's Ghost identity is
  narrative/gym-roster, not wild-table. No changes made.
