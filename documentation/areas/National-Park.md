# National Park

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers both the normal-day encounter table and the Bug-Catching Contest variant, since
they're the same map (`MAP_D22R0101`) with two different `EncounterData` entries swapped in
depending on contest state.

## Header facts

- **ENCDATA constants:** `ENCDATA_D22R0101_NATIONAL_PARK` (`data/Encounters.c:2309`, normal),
  `ENCDATA_D22R0102_NATIONAL_PARK_BUG_CATCHING_CONTEST` (`data/Encounters.c:2409`, contest-active)
- **Map constants:** `MAP_D22R0101` (`include/constants/maps.h:100`, normal field),
  `MAP_D22R0102` (`include/constants/maps.h:491`, contest field — separate map ID despite sharing
  the "National Park" name)
- **Connects:** Route 35 (south) ↔ Route 36 (north).
- **Leads toward:** Morty (Ecruteak City) — middle leg of the Route 35 → National Park →
  Route 36 → Ecruteak corridor.
- **Biome Map tie-in:** same Morty-row Dark-coverage gap as Route 35/36 — see Notes. No change
  made here; Route 36 is where the fix lands (last route before the gym).

## Encounter methods active

Identical for both variants — this is a walk-only field, no water/rod methods.

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table — normal (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 10 | Caterpie | Caterpie | Hoothoot |
| 2 | 20 | 10 | Metapod | Metapod | Hoothoot |
| 3 | 10 | 10 | Caterpie | Caterpie | Hoothoot |
| 4 | 10 | 10 | Metapod | Metapod | Hoothoot |
| 5 | 10 | 12 | Caterpie | Sunkern | Hoothoot |
| 6 | 10 | 12 | Caterpie | Sunkern | Hoothoot |
| 7 | 5 | 12 | Pidgey | Pidgey | Hoothoot |
| 8 | 5 | 12 | Pidgey | Pidgey | Hoothoot |
| 9 | 4 | 10 | Pidgey | Sunkern | Hoothoot |
| 10 | 4 | 14 | Pidgey | Pidgey | Hoothoot |
| 11 | 1 | 10 | Pidgey | Sunkern | Hoothoot |
| 12 | 1 | 14 | Pidgey | Pidgey | Hoothoot |

Night is 100% Hoothoot regardless of slot — this field is Hoothoot-only after dark.

## Land encounter table — Bug-Catching Contest variant (walk, rate 25)

100% Caterpie, every slot, every time of day. Rustling grass is also 100% Caterpie (both sound
regions). This is the intentional vanilla contest gimmick (everyone catches the same easy species
during the event) — not a curation gap, don't touch it.

## Rustling grass (Hoenn/Sinnoh sound species) — normal variant only

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- Normal variant: `landSwarm = SPECIES_CATERPIE`. Contest variant: same.
- **Inert:** neither `MAP_D22R0101` nor `MAP_D22R0102` is in `sSwarmMapLUT` (`src/swarms.c`).

## Headbutt trees (`data/Headbutt.c`, `.nationalPark`)

Real tree data here (22 normal-tier trees + 5 special-tier trees, not an empty placeholder like
most gate/connector maps) — one of the few areas in this corridor with headbutt content worth
tracking.

| Species | Type(s) | Regional Dex # | Tier | Level |
|---|---|---|---|---|
| Hoothoot | Normal/Flying | 13 | Normal | 10–15 |
| Pineco | Bug | 76 | Normal | 10–12 |
| Exeggcute | Grass/Psychic | 82 | Normal, Special | 10–20 |
| Spinarak | Bug/Poison | 28 | Normal | 13–15 |
| Cherubi | Grass | **not in regional dex** | Special | 18–25 |

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day |
| Hoothoot | Normal/Flying | 13 | Walk, Headbutt | Night (walk) / any (headbutt) |
| Sunkern | Grass | 80 | Walk | Day |
| Pineco | Bug | 76 | Headbutt | — |
| Spinarak | Bug/Poison | 28 | Headbutt | — |
| Exeggcute | Grass/Psychic | 82 | Headbutt | — |
| Caterpie | Bug | 20 | Walk, Swarm (land, inert) | Morning/Day (normal); all day (contest) |
| Metapod | Bug | 21 | Walk | Morning/Day |
| Cherubi | Grass | **not in regional dex** | Headbutt (special tier) | — |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- No dex/encounter mismatches here — every walked/headbutt species (Pidgey, Hoothoot, Sunkern,
  Caterpie, Metapod, Pineco, Spinarak, Exeggcute) is already regional-dex-tracked. Cherubi
  (headbutt special tier only) is the lone dex-less entry and it's a routine cut, not an
  evolution-mismatch case like Slowpoke was.
- Plusle/Minun/Shinx (all three rustling-grass slots here) are `keep = Yes` in the curation sheet
  — unlike most rustling-grass filler seen elsewhere on this corridor (Route 35's Whismur/
  Linoone/Buizel/Bidoof are all cut). Nothing to fix, just worth noting these are real
  encounters if a player triggers them, not disposable flavor.
- No Dark-type here either. Same as Route 35 — not this area's fix to make; see Route-36.md.
- Bug-Catching-Contest variant is intentionally monotype/single-species by design (vanilla
  minigame behavior) — excluded from any type-coverage-audit consideration.
