# Dark Cave (Route 31 Entrance)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D42R0102_DARK_CAVE_ROUTE_31_ENTRANCE` (`data/Encounters.c:6909`)
- **Map constant:** `MAP_D42R0102` (`include/constants/maps.h:180`)
- **Connects:** Route 31 ↔ deeper Dark Cave (eventually to the Route 45/46 side, via
  `ENCDATA_D42R0101_DARK_CAVE_ROUTE_45_ENTRANCE`, not covered by this doc).
- **Leads toward:** Falkner (Violet City) — optional side-detour off Route 31, not mandatory to
  reach the gym.
- **Biome Map tie-in:** this is the area `HACK_PLAN.md`'s Falkner row explicitly names as the Rock
  counter source: "Rock via Geodude (Dark Cave/Route 31, already vanilla-natural)." Confirmed —
  Geodude is this area's dominant land species.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 50 | Yes (highest rate of any Falkner-approach area) |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

Notably lower walk rate (10, vs. 25 on the routes) but a much higher Rock Smash rate — consistent
with a cave interior where wall-cracking is the primary interaction, not grass-walking.

## Land encounter table (walk, rate 10)

Identical across morning/day/night — caves have no time-of-day variation here.

| Slot | % | Level | Species |
|---|---|---|---|
| 1 | 20 | 3 | Geodude |
| 2 | 20 | 2 | Zubat |
| 3 | 10 | 3 | Geodude |
| 4 | 10 | 2 | Zubat |
| 5 | 10 | 2 | Geodude |
| 6 | 10 | 2 | Geodude |
| 7 | 5 | 4 | Geodude |
| 8 | 5 | 4 | Geodude |
| 9 | 4 | 3 | Zubat |
| 10 | 4 | 4 | Zubat |
| 11 | 1 | 3 | Zubat |
| 12 | 1 | 4 | Dunsparce |

## Water/rod tables

**Surf (rate 10):** Magikarp in all 5 slots (60/30/5/4/1%, levels 10–20/5–15/2–10/2–10/2–10) —
a small underground stream, not a real water route.
**Rock Smash (rate 50, 90/10):** Dunsparce (4–8), Geodude (8–14)
**Old Rod (60/30/5/4/1):** Magikarp ×3, Wooper ×2 (all level 10)
**Good Rod (40/40/15/4/1):** Magikarp, Wooper ×4 (all level 20)
**Super Rod (40/40/15/4/1):** Wooper ×2, Magikarp, Quagsire, Magikarp (all level 40)

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

Same mechanic as the outdoor routes despite being a cave interior — "grass" rustling here is a
vanilla quirk of this being the map's registered sound-encounter table, not a literal patch of
grass underground.

## Swarm

- `landSwarm = SPECIES_DUNSPARCE`, `surfSwarm = SPECIES_MAGIKARP`, `fishSwarm = SPECIES_MAGIKARP`,
  `nightFish = SPECIES_WOOPER`
- **Active, unlike every other Falkner-approach area documented so far:** `MAP_D42R0102` **is** in
  `sSwarmMapLUT` (`src/swarms.c`, `SWARM_GRASS` type). On the days this map rolls for the swarm,
  wild Geodude/Zubat/Dunsparce encounters here are replaced with a Dunsparce swarm. Worth knowing
  before touching `landSwarm` — it isn't dead weight here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk/Rock Smash | All |
| Zubat | Poison/Flying | **not in regional dex** | Walk | All |
| Dunsparce | Normal | 45 | Walk/Rock Smash | All |
| Magikarp | Water | 65 | Surf/Fish | — |
| Wooper | Water/Ground | 49 | Fish | — |
| Quagsire | Water/Ground | 50 | Fish | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Makuhita | Fighting | **not in regional dex** | Rustling grass (Hoenn) | — |
| Bronzor | Steel/Psychic | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- **Zubat is dex-less, and this is a resolved evolution-chain question, not an open one:** the
  curation sheet marks `keep=No` for the entire Zubat → Golbat → Crobat line. Before the
  [[dex-curation]] sync fix this session, Crobat was still sitting in `data/RegionalDex.c` despite
  that — a leftover that's now been corrected (Crobat removed). So Zubat staying dex-less here is
  consistent and intentional, not a mismatch needing a swap-in like Route 29's Rattata.
- **Geodude confirms the Biome Map's Falkner counter-access note** — it's genuinely the dominant
  species here (2 of the top-2 slot weights), so the "Rock via Geodude, already vanilla-natural"
  claim in `HACK_PLAN.md` holds up against the actual data.
- **Resolved — Goldeen/Seaking → Wooper/Quagsire**, across all Old/Good/Super Rod slots that held
  them (Goldeen in Old Rod ×2, Good Rod ×4, Super Rod ×2; Seaking in Super Rod ×1) plus
  `nightFish`. Both were dex-less (`keep=No` in the curation sheet) — note this is *not* the same
  pattern as Route 30/31's fishing tables, which only ever carried Magikarp/Poliwag, not
  Goldeen/Seaking; that cross-reference in an earlier draft of this note was wrong. Wooper/Quagsire
  (Water/Ground, #49/#50, both `keep=Yes`) replace them: thematically a better fit for a cave
  stream than an open-water fish line, and stat-comparable (Wooper BST 210 vs. Goldeen 320 — a
  power *decrease*; Quagsire BST 430 vs. Seaking 450 — near-identical), so the Super Rod's rare
  Quagsire slot still reads as "the evolved form as an uncommon catch," same as vanilla Rod-table
  design.
- **Type-coverage relevance (Pillar 3) — this closes out the Falkner pre-gym audit.** Status as of
  Route 30's Rattata → Shinx swap (see that doc's Notes): Rock is covered here (Geodude, dominant
  land species) and Electric is covered by Route 30's night-only Shinx — both wild-caught, both
  reachable before Violet City. As of the Route 29 Cutiefly swap there's also a Fairy-typed mon on
  the approach (not itself a Rock/Electric/Ice counter, but notable for the hack's Fairy presence).
  **Ice is the one type in Falkner's Rock/Electric/Ice weakness set with no pre-gym wild option**,
  and that's accepted rather than an open gap to fix: vanilla Johto has no naturally-occurring wild
  Ice type this early either (first one is out past Ice Path), and Pillar 3 is explicitly a soft
  preference, not a hard gate — Rock + Electric is a real, wild-caught counter path into Falkner,
  which is what the audit requires. Nothing further to change on this area for the Falkner pass.
