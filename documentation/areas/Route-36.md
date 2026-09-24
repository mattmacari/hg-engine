# Route 36

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R36_ROUTE_36` (`data/Encounters.c:2509`)
- **Map constant:** `MAP_R36` (`include/constants/maps.h:44`)
- **Connects:** National Park (south) ↔ Ecruteak City (north). (Route 37 also branches off this
  route, but it leads onward past Ecruteak toward Olivine — not part of the approach to Morty.)
- **Leads toward:** Morty (Ecruteak City) — this is the last route before the gym, same role
  Route 33 played for Bugsy and Route 34 played for Whitney.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Morty row counter-access note: "Dark needed (Ghost's
  other weakness besides Ghost itself)." The plan's original text assumed "Murkrow already spawns
  near National Park at night in vanilla" — that assumption doesn't hold in this codebase's
  current encounter tables: `grep`ing `SPECIES_MURKROW` in `data/Encounters.c` only turns up Route
  7 and Route 16, both Kanto, both far past Ecruteak. Route 35/National Park (documented above)
  also have no Dark-type. See Notes for the fix made here.

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
| 1 | 20 | 12 | Teddiursa | Teddiursa | Teddiursa |
| 2 | 20 | 12 | Woobat | Woobat | Woobat |
| 3 | 10 | 12 | Teddiursa | Teddiursa | Teddiursa |
| 4 | 10 | 12 | Woobat | Woobat | **Murkrow** |
| 5 | 10 | 13 | Pidgey | Pidgey | Hoothoot |
| 6 | 10 | 13 | Pidgey | Pidgey | Hoothoot |
| 7 | 5 | 13 | Growlithe | Growlithe | Growlithe |
| 8 | 5 | 13 | Growlithe | Growlithe | Growlithe |
| 9 | 4 | 13 | Stantler | Stantler | Stantler |
| 10 | 4 | 15 | Pidgey | Growlithe | Hoothoot |
| 11 | 1 | 13 | Stantler | Stantler | Stantler |
| 12 | 1 | 15 | Pidgey | Growlithe | Hoothoot |

Slot 4 is the only slot that varies by time of day here — morning/day stay Nidoran♀, night is
Murkrow (see Notes).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_TEDDIURSA`.
- **Inert:** `MAP_R36` is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day |
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Growlithe | Fire | 99 | Walk | Morning/Day/Night |
| Stantler | Normal | 101 | Walk | Morning/Day/Night |
| Murkrow | Dark/Flying | 161 | Walk | Night (slot 4 only) |
| Teddiursa | Normal | 151 | Walk, Swarm (land, inert) | Morning/Day/Night |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day (slot 4 night is now Murkrow) |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Resolved — Dark-type coverage gap closed here.** Replaced slot 4's night-only entry (10%,
  previously Nidoran♀, same species still present morning/day at that slot) with **Murkrow**.
  Night-only placement matches Murkrow's own flavor (nocturnal crow) and leaves the Nidoran line
  otherwise fully intact morning/day and in the other three Nidoran slots. No curation-sheet
  change was needed — Murkrow was already regional-dex-tracked (`keep = Yes`, #161) despite not
  spawning anywhere on this corridor.
- Growlithe here was already present in the base data (separate from the Growlithe this project
  added to Route 33 for Bugsy's Fire-coverage gap) — no relation, just a coincidental pre-existing
  Fire-type on this route.
- **Resolved — Nidoran♂/♀ replaced (60% of the table before the Murkrow split).** Replaced with
  **Teddiursa** and **Woobat**, both already regional-dex-tracked (#151/#276) and not spawning
  anywhere else in the build. Teddiursa echoes the forest biome of National Park one area south;
  Woobat continues the Psychic thread running through this whole corridor (Abra on Route 34/35,
  Wynaut on Route 35). Slot 4's night-only Murkrow (resolved separately, see below) is untouched.
- This route's Dark gap mirrors Bugsy's Fire gap and Whitney's Fighting gap almost exactly: the
  fix lands on the last route before the gym, replacing part of an already-dex-cut, high-share
  filler species rather than introducing a new slot or removing something outright.
