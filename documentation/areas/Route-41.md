# Route 41

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_W41_ROUTE_41` (`data/Encounters.c:4209`)
- **Map constant:** `MAP_W41` (`include/constants/maps.h:99`)
- **Connects:** Route 40 (north) ↔ Cianwood City (south).
- **Leads toward:** Chuck (Cianwood City) — second/final leg of the Olivine→Cianwood sea crossing.
  Pure water route — no land tile at all (`rateWalk = 0`).
- **Biome Map tie-in:** same as Route 40 — this and Route 40 together are the "stormy coastal"
  crossing `HACK_PLAN.md`'s Chuck row describes.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 0 | No (pure water route, no land tile) |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 10):** Staryu (15%), Starmie (15%), Mantine ×3 (15/15/15%).
**Old Rod (10/10/10/10/10):** Magikarp ×3, Staryu ×2 (all level 10).
**Good Rod (20/20/20/20/20):** Magikarp, Staryu, Chinchou ×2, Shellder (all level 20).
**Super Rod (40/40/40/40/40):** Chinchou, Shellder, Starmie ×2, Lanturn (all level 40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile on this route.

## Swarm

- `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_SHELLDER`, `fishSwarm = SPECIES_MAGIKARP`.
  `landSwarm = SPECIES_NONE` (no grass tile to swarm on).
- **Inert:** `MAP_W41` is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Mantine | Water/Flying | 155 | Surf | — |
| Chinchou | Water/Electric | 132 | Fish | — |
| Lanturn | Water/Electric | 133 | Fish | — |
| Shellder | Water/Ice | 127 | Fish (night) | — |
| Staryu | Water | 125 | Surf, Fish, Swarm (surf) | — |
| Starmie | Water/Psychic | 126 | Surf, Fish | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Resolved — Tentacool/Tentacruel replaced.** Unlike Route 40, this route's rod tables were
  already mostly dex-tracked (Chinchou/Lanturn/Shellder), so the fix here was narrower — just the
  Surf slot not taken by Mantine plus the Tentacool/Tentacruel remnants scattered across the rod
  tiers. Replaced with **Staryu/Starmie**, matching the same fix applied on Route 40 and Cianwood
  City — the whole Olivine↔Cianwood crossing shares one pool, so keeping the family consistent
  across all three areas reads as one coherent marine ecosystem rather than three patched-up ones.
- Mantine being present and dex-tracked (#155) means this route already has a strong, correct
  Water/Flying centerpiece — untouched by this pass.
- No land tile, so no Flying/Psychic/Fairy counter-access contribution — see Cianwood-City.md's
  Notes for the full coverage-audit writeup (already resolved, no gap).
