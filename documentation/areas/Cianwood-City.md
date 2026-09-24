# Cianwood City

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T24_CIANWOOD_CITY` (`data/Encounters.c:5109`)
- **Map constant:** `MAP_T24` (`include/constants/maps.h:79`)
- **Connects:** Route 41 (Surf, north) — Cianwood is an island, only reachable by Surf.
- **Leads toward:** Chuck — this is the gym's own city. No land walk encounters (city tile), only
  water/fishing/Rock Smash.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Chuck row: "Cianwood is a stormy coastal island reached
  by Surf — genuinely fits a rain/ocean archetype." That's about the city/gym's own flavor; see
  Notes below for the type-coverage audit (Flying/Psychic/Fairy) the plan flagged as needing
  confirmation before this gym.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 0 | No (city tile, no grass) |
| Surf | 15 | Yes |
| Rock Smash | 30 | Yes |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 15):** Staryu ×2 (15/10%), Starmie ×3 (15/15/15%).
**Rock Smash (rate 30):** Shellder (level 15–24), Shuckle (level 23–28).
**Old Rod (10/10/10/10/10):** Magikarp ×3, Shellder ×2 (all level 10).
**Good Rod (20/20/20/20/20):** Magikarp, Shellder ×3, Corsola (all level 20).
**Super Rod (40/40/40/40/40):** Shellder ×3, Corsola, Cloyster (all level 40).

Identical Surf/rod tables to Route 40 — this whole stretch shares one fishing/surf pool.

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile in this city.

## Swarm

- `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_STARYU`, `fishSwarm = SPECIES_MAGIKARP`.
  `landSwarm = SPECIES_NONE` (no grass tile to swarm on).
- **Inert:** `MAP_T24` is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Corsola | Water/Rock | 129 | Fish | — |
| Shuckle | Bug/Rock | 124 | Rock Smash | — |
| Staryu | Water | 125 | Surf, Fish (night), Swarm (surf) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water/Ice | 127 | Rock Smash, Fish | — |
| Cloyster | Water/Ice | 128 | Fish | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- **Resolved — Tentacool/Tentacruel/Krabby/Kingler replaced**, matching the identical fix applied
  on Route 40 (see Route-40.md's Notes for the full reasoning): Tentacool/Tentacruel → Staryu/
  Starmie, Krabby/Kingler → Shellder/Cloyster. Also applied to the Rock Smash slot (Krabby →
  Shellder), which Route 40 doesn't have. Shuckle (Rock Smash) was already tracked and is
  untouched.
- **Type-coverage audit for Chuck (Fighting — weak to Flying/Psychic/Fairy), resolved:**
  `HACK_PLAN.md`'s original text guessed "Flying already covered (Zubat/Golbat on the water
  route)" and "Fairy... Jigglypuff/Igglybuff already spawn on the Route 47/48 approach — confirm
  availability before Cianwood." Both guesses were wrong in the specifics (same pattern as the
  Morty-row Murkrow assumption that also didn't hold) — checked against the actual data:
  - **Flying:** Zubat/Golbat don't spawn on Route 40/41 at all, but they're not needed to —
    Zubat is already available from **Union Cave** and **Slowpoke Well**, both visited well before
    Bugsy, let alone Chuck. Flying coverage has been available since the *second* gym. (Zubat/
    Golbat themselves are dex-less, same routine cut as everywhere — doesn't block catching them,
    just won't register a dex entry.)
  - **Psychic:** Abra has been available since Route 34/35 (pre-Whitney). Already covered.
  - **Fairy:** Route 47/48 is real content but it's deep post-Mt.-Silver Kanto — nowhere near
    reachable before Cianwood, so that specific claim was wrong. The actual pre-Cianwood Fairy
    access is **Snubbull on Route 38** (1% slot, night-excluded — see `data/Encounters.c:3809`),
    which the player does pass through en route to Olivine before Surfing to Cianwood. Snubbull is
    dex-tracked (#95). It's a thin single-slot foothold rather than a robust option — worth a
    dedicated Jasmine-corridor pass later if it needs strengthening, but the coverage technically
    exists and isn't a gap that blocks the fight.
  - **Net result:** no new species needs to be introduced anywhere in this corridor for Chuck's
    counter-access — all three types are already reachable pre-gym. `HACK_PLAN.md`'s Chuck row
    should be updated to reflect the corrected sourcing (done alongside this doc).
