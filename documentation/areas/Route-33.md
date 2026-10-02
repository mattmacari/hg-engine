# Route 33

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R33_ROUTE_33` (`data/Encounters.c:1709`)
- **Map constant:** `MAP_R33` (`include/constants/maps.h:41`)
- **Connects:** Union Cave's south exit ↔ Azalea Town.
- **Leads toward:** Bugsy (Azalea Town) — final leg before the gym.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Bugsy row counter-access note: "Fire/Flying/Rock needed.
  Flying already covered from Falkner-approach routes. Consider an earlier Fire option (e.g.
  Growlithe pulled forward) so Fire isn't first available much later." This route is the last
  option before Azalea Town/Bugsy for placing that Fire pickup — see Notes.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 6 | Hoppip | Hoppip | Woobat |
| 2 | 20 | 7 | Ekans | Ekans | Ekans |
| 3 | 10 | 6 | Hoppip | Hoppip | Woobat |
| 4 | 10 | 7 | Ekans | Ekans | Ekans |
| 5 | 10 | 6 | Growlithe | Growlithe | Ekans |
| 6 | 10 | 6 | Growlithe | Growlithe | Ekans |
| 7 | 5 | 6 | Ekans | Ekans | Ekans |
| 8 | 5 | 6 | Ekans | Ekans | Ekans |
| 9 | 4 | 8 | Hoppip | Hoppip | Woobat |
| 10 | 4 | 4 | Woobat | Ekans | Woobat |
| 11 | 1 | 8 | Hoppip | Hoppip | Woobat |
| 12 | 1 | 4 | Woobat | Ekans | Woobat |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_HOPPIP`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Ekans | Poison | 43 | Walk | Morning/Day/Night |
| Hoppip | Grass/Flying | 60 | Walk, Swarm (land) | Morning/Day |
| Growlithe | Fire | 99 | Walk | Morning/Day |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Night |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** Rattata → **Ekans** (#43,
  continuing from Route 32 through Union Cave), Zubat → **Woobat** (#276). Earlier notes below that describe these species as dex-less or intentionally kept are superseded.
- Rattata/Zubat dex-less here is the routine curation-sheet cut (`keep = No` in
  `data/generated/species_dex_meta.csv`), consistent with every other Falkner/Bugsy-approach doc.
- **Resolved — Fire-type coverage gap closed here.** Replaced Spearow (already dex-cut, contributing
  nothing) at slots 5–6 with Growlithe (10% each, level 6, morning/day) per `HACK_PLAN.md`'s
  suggestion to pull an earlier Fire option forward. This was the natural replacement candidate:
  removing it doesn't lose any dex-tracked species, and it's the last land route before Azalea
  Town/Bugsy, so it's genuinely available before the gym rather than first appearing after. Spearow
  is gone from this route entirely now (was the route's only Flying-type, but already contributed
  nothing to the "Flying already covered" claim while dex-cut).
- This route has zero water encounters — matches vanilla Route 33's actual geography (landlocked
  between two cave/town nodes), not an oversight.
- Hoppip is reused a third time on this leg (Route 31's night-slot Rattata backfill, Route 32's own
  natural placement, now here) — by this point it's clearly the "default Grass/Flying filler"
  across the whole Falkner-through-Bugsy corridor. Left as-is here since the Fire-gap fix didn't
  touch Hoppip's slots, but worth knowing before adding a fourth placement elsewhere.
