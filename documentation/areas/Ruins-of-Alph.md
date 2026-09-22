# Ruins of Alph (Outside / Inside Main Room / Inside Ladder Room)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers all three *used* sub-areas in one doc (see Notes for the two unused variants that
are deliberately skipped).

## Header facts

- **ENCDATA constants:**
  - `ENCDATA_D24R0101_RUINS_OF_ALPH_OUTSIDE` (`data/Encounters.c:909`)
  - `ENCDATA_D24R0205_RUINS_OF_ALPH_INSIDE_MAIN_ROOM` (`data/Encounters.c:1109`)
  - `ENCDATA_D24R0217_RUINS_OF_ALPH_INSIDE_LADDER_ROOM` (`data/Encounters.c:1309`)
- **Map constants:** `MAP_D24R0101` (`include/constants/maps.h:117`),
  `MAP_D24R0205` (`include/constants/maps.h:319`),
  `MAP_D24R0217` (`include/constants/maps.h:495`)
- **Connects:** an optional detour off Route 32 (west side), loops back to Route 32 — not on the
  critical path to Azalea Town.
- **Leads toward:** Bugsy (Azalea Town), as an optional side area encountered along the way.
- **Biome Map tie-in:** not called out by name in `HACK_PLAN.md`'s Bugsy row (which focuses on
  Ilex Forest's bug variety and the Fire/Flying/Rock counter-access note). This area's own flavor
  is Psychic/puzzle (Unown) rather than Bug, so it's peripheral to Bugsy's own archetype — but see
  Notes for a genuine Rock-counter contribution via Rock Smash.

## Encounter methods active

### Outside

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 20 | Yes |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

### Inside (Main Room / Ladder Room)

| Method | Rate | Active? |
|---|---|---|
| Walk | 15 | Yes — Unown only |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table

### Outside (walk, rate 10)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 20 | Natu | Natu | Natu |
| 2 | 20 | 22 | Natu | Natu | Natu |
| 3 | 10 | 20 | Natu | Natu | Natu |
| 4 | 10 | 22 | Natu | Natu | Natu |
| 5 | 10 | 18 | Natu | Natu | Natu |
| 6 | 10 | 18 | Natu | Natu | Natu |
| 7 | 5 | 24 | Natu | Natu | Natu |
| 8 | 5 | 24 | Natu | Natu | Natu |
| 9 | 4 | 20 | Smeargle | Smeargle | Smeargle |
| 10 | 4 | 22 | Smeargle | Smeargle | Smeargle |
| 11 | 1 | 20 | Smeargle | Smeargle | Smeargle |
| 12 | 1 | 22 | Smeargle | Smeargle | Smeargle |

Identical across all three time windows — Natu/Smeargle only, no day/night variation.

### Inside — Main Room and Ladder Room (walk, rate 15) — identical, Unown only

All 12 slots, all three time windows: `SPECIES_UNOWN`, level 5.

## Water/rod tables (Outside only)

**Surf (rate 10):** Wooper (10–20, 60%), Quagsire ×4 (15–25/10–20/10–20/10–20, 30/5/4/1%).
**Rock Smash (rate 20):** Geodude ×2 (8–14, 90%; 3–6, 10%).
**Old Rod (60/30/5/4/1):** Magikarp ×3, Poliwag ×2 (all level 10).
**Good Rod (40/40/15/4/1):** Magikarp, Poliwag ×4 (all level 20).
**Super Rod (40/40/15/4/1):** Poliwag ×2, Magikarp, Poliwag, Magikarp (all level 40).

## Rustling grass (Hoenn/Sinnoh sound species) — Outside only

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

Inside (Main Room / Ladder Room): both slots are `SPECIES_UNOWN` in both hoennSoundSpecies and
sinnohSoundSpecies — not a real rustling-grass encounter, just the struct's default/unused state
for an indoor puzzle room (rate 0 methods elsewhere reinforce this reads as inert filler, not a
deliberate design choice to make).

## Swarm

- **Outside:** `landSwarm = SPECIES_NATU`, `surfSwarm = SPECIES_WOOPER`. Neither `MAP_D24R0101` nor
  the inside rooms' map constants appear in `sSwarmMapLUT` (`src/swarms.c`) — inert.
- **Inside (both rooms):** `landSwarm = SPECIES_UNOWN` — also inert, same reason.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Natu | Psychic/Flying | 121 | Walk | Morning/Day/Night |
| Smeargle | Normal | 119 | Walk | Morning/Day/Night |
| Unown | Psychic | 54 | Walk (inside) | Morning/Day/Night |
| Wooper | Water/Ground | 49 | Surf | — |
| Quagsire | Water/Ground | 50 | Surf | — |
| Geodude | Rock/Ground | 30 | Rock Smash | — |
| Magikarp | Water | 65 | Fish | — |
| Poliwag | Water | 346 | Fish | — |
| Whismur | Normal | **not in regional dex** | Rustling grass (Hoenn, outside) | — |
| Linoone | Normal | **not in regional dex** | Rustling grass (Hoenn, outside) | — |
| Buizel | Water | **not in regional dex** | Rustling grass (Sinnoh, outside) | — |
| Bidoof | Normal | **not in regional dex** | Rustling grass (Sinnoh, outside) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this area's tables are finalized.

## Notes

- Every species that appears on this area's active tables is already dex-tracked — no cuts to flag
  here, unlike most of the other Bugsy-approach areas.
- **Two unused variants deliberately skipped:** `ENCDATA_D24R0216_RUINS_OF_ALPH_INSIDE_MAIN_ROOM_UNUSED`
  and `ENCDATA_D24R0218_RUINS_OF_ALPH_INSIDE_MAIN_ROOM_UNUSED` are byte-identical placeholder
  copies of the Main Room table (`SPECIES_UNOWN` everywhere, rate 15) that no live map references —
  matches the general "UNUSED_0##" pattern seen throughout `data/Encounters.c`. Not documented as
  their own areas since nothing reads them.
- **Type-coverage relevance (Pillar 3, Bugsy):** Rock Smash here gives a second wild Geodude source
  beyond Route 31/Dark Cave (already Falkner's Rock answer) — not load-bearing for Bugsy's own
  Fire/Flying/Rock counter-access note since Rock isn't one of Bugsy's needed counters (Bugsy is
  weak to Fire/Flying/Rock, so *these* are what the player needs going in, and Geodude doesn't help
  against a Bug gym — it's listed here for completeness, not as a Bugsy-relevant find).
- Outside's surf/rod tables (Wooper/Quagsire/Magikarp/Poliwag) match Route 32's water-adjacent
  shape rather than introducing anything new — consistent regional water fauna, no notes needed.
- Optional/side-area status means this is lower priority than Route 33/Union Cave/Ilex Forest for
  the Bugsy audit — flagged here for completeness, not because anything needs fixing before Bugsy's
  roster work starts.
