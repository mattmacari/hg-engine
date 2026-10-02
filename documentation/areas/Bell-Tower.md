# Bell Tower (2F–10F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. All nine floors have byte-identical encounter tables, so they're collapsed into one set of
tables (2F shown), the same approach as Sprout Tower.

## Header facts

- **ENCDATA constants** (`data/Encounters.c` line): `ENCDATA_D17R0102_BELL_TOWER_2F` (3009),
  `_3F` (3109), `_4F` (3209), `_5F` (3309), `_6F` (3409), `_7F` (3509), `_8F` (3609), `_9F` (3709),
  `ENCDATA_D17R0112_BELL_TOWER_10F` (8409).
- **Map constants:** `MAP_D17R0102`–`MAP_D17R0109` (`include/constants/maps.h:336–343`),
  `MAP_D17R0112` (`:345`).
- **Connects:** Ecruteak City (north side, through the Wise Trio's gate).
- **Leads toward:** Ho-Oh at the summit — story-gated (Clear Bell, then the Rainbow Wing), so this is
  late/optional content rather than a gym corridor. The Ho-Oh encounter is scripted, not in these
  tables.
- **Biome Map tie-in:** Ecruteak's ghost lore (`HACK_PLAN.md`'s Morty row), the sacred-tower
  counterpart to the Burned Tower.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 20 | Misdreavus | Misdreavus | Gastly |
| 2 | 20 | 21 | Drifloon | Drifloon | Gastly |
| 3 | 10 | 20 | Misdreavus | Misdreavus | Gastly |
| 4 | 10 | 21 | Drifloon | Drifloon | Gastly |
| 5 | 10 | 22 | Misdreavus | Misdreavus | Gastly |
| 6 | 10 | 22 | Drifloon | Drifloon | Gastly |
| 7 | 5 | 22 | Drifloon | Drifloon | Misdreavus |
| 8 | 5 | 22 | Misdreavus | Misdreavus | Drifloon |
| 9 | 4 | 23 | Gastly | Gastly | Misdreavus |
| 10 | 4 | 24 | Gastly | Gastly | Drifloon |
| 11 | 1 | 23 | Gastly | Gastly | Misdreavus |
| 12 | 1 | 24 | Gastly | Gastly | Drifloon |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Zigzagoon | Spinda |
| Sinnoh | Chatot | Meditite |

## Swarm

- `landSwarm = SPECIES_DRIFLOON`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** no Bell Tower floor is in `sSwarmMapLUT` (`src/swarms.c`), so the land swarm never fires. Activating it would mean editing the shared engine swarm table, which also drives the daily swarm rotation.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Gastly | Ghost/Poison | 51 | Walk | Morning/Day/Night |
| Misdreavus | Ghost | 167 | Walk | Morning/Day/Night |
| Drifloon | Ghost/Flying | 238 | Walk, Swarm (land) | Morning/Day/Night |
| Chatot | Normal/Flying | **not in dex** | Rustling grass (Sinnoh) | — |
| Meditite | Fighting/Psychic | **not in dex** | Rustling grass (Sinnoh) | — |
| Spinda | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Zigzagoon | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Rattata removed (Bell Tower pass).** Rattata (dex-less) filled every day/morning
  slot and the six low-weight night slots (20% at night). Replaced with two Ghost types that fit a
  sacred bell tower, alongside Gastly:
  - **Misdreavus** (#167): a Johto-native ghost in Morty's city. It also echoes the Misdreavus on
    Morty's own team, which previews the Mismagius on his rematch team.
  - **Drifloon** (#238, Ghost/Flying): a drifting balloon spirit that suits a wind-swept tower with
    a legendary bird at the top. It was dex-tracked but spawned nowhere until now.
- **Split:**
  - Day/morning: Misdreavus 45%, Drifloon 45%, Gastly 10% (Gastly takes the four rare slots, so
    the tower is haunted at all hours).
  - Night: Gastly keeps its 80%; Misdreavus and Drifloon take 10% each in the old Rattata slots.
  - The land swarm field is now Drifloon, but it's inert (see Swarm).
- **Left as-is:** dex-less rustling-grass species (post-game only).
