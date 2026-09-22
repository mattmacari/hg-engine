# Route 32

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R32_ROUTE_32` (`data/Encounters.c:809`)
- **Map constant:** `MAP_R32` (`include/constants/maps.h:40`)
- **Connects:** Violet City (north) ↔ the Ruins of Alph turnoff / Union Cave approach (south);
  Union Cave in turn leads on to Route 33 and Azalea Town.
- **Leads toward:** Bugsy (Azalea Town) — first leg of the approach, though this route was already
  touched once during Falkner's pass (see below).
- **Biome Map tie-in:** `HACK_PLAN.md`'s Bugsy row: "Ilex Forest is already a deep-forest biome —
  canon-correct, just deepen bug variety (Scyther/Pinsir via Headbutt trees)" and counter-access
  note "Fire/Flying/Rock needed. Flying already covered from Falkner-approach routes. Consider an
  earlier Fire option (e.g. Growlithe pulled forward)." This route's own table carries none of
  Fire/Flying/Rock — see Notes.
- **Falkner carry-over:** this route's Notes in `HACK_PLAN.md`'s Falkner row call for "pulling
  Mareep earlier onto Route 32's farmland edge for an Electric option" — that edit is already live
  in the table below (Mareep occupies slots 5–6 morning/day). This doc is the first time the area
  itself gets written up, even though the table was touched during the Falkner pass.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 6 | Bellsprout | Bellsprout | Wooper |
| 2 | 20 | 4 | Rattata | Rattata | Rattata |
| 3 | 10 | 6 | Bellsprout | Bellsprout | Wooper |
| 4 | 10 | 4 | Rattata | Rattata | Rattata |
| 5 | 10 | 6 | **Mareep** | **Mareep** | Bellsprout |
| 6 | 10 | 6 | **Mareep** | **Mareep** | Bellsprout |
| 7 | 5 | 6 | Hoppip | Hoppip | **Mareep** |
| 8 | 5 | 6 | Hoppip | Hoppip | **Mareep** |
| 9 | 4 | 6 | Rattata | Rattata | Wooper |
| 10 | 4 | 4 | Zubat | Rattata | Zubat |
| 11 | 1 | 6 | Rattata | Rattata | Wooper |
| 12 | 1 | 4 | Zubat | Rattata | Zubat |

## Water/rod tables

**Surf (rate 15):** Tentacool (10–20, 60%), Quagsire (15–25, 30%), Tentacruel ×3 (15–25/15–25/36,
5/4/1%).
**Old Rod (60/30/5/4/1):** Magikarp ×3, Tentacool ×2 (all level 10).
**Good Rod (40/40/15/4/1):** Magikarp, Tentacool ×3, Qwilfish (all level 20).
**Super Rod (40/40/15/4/1):** Tentacool ×2, Magikarp, Qwilfish, Magikarp (all level 40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_BELLSPROUT`, `surfSwarm = SPECIES_TENTACOOL`, `nightFish = SPECIES_TENTACOOL`,
  `fishSwarm = SPECIES_QWILFISH`.
- **Active:** `MAP_R32` **is** in `sSwarmMapLUT` (`src/swarms.c`) as a `SWARM_FISHING` entry — the
  daily swarm mechanic can actually put a Qwilfish swarm on this route's fishing spots. First area
  in the Bugsy-approach set (so far) where the swarm field isn't inert — worth remembering if
  `fishSwarm` ever gets rebalanced here, since it's live.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Bellsprout | Grass/Poison | 57 | Walk | Morning/Day/Night |
| Mareep | Electric | 46 | Walk | Morning/Day/Night |
| Hoppip | Grass/Flying | 60 | Walk | Morning/Day |
| Wooper | Water/Ground | 49 | Walk | Night |
| Rattata | Normal | **not in regional dex** | Walk | Morning/Day/Night |
| Zubat | Poison/Flying | **not in regional dex** | Walk | Morning/Night |
| Tentacool | Water/Poison | **not in regional dex** | Surf/Fish | — |
| Tentacruel | Water/Poison | **not in regional dex** | Surf | — |
| Quagsire | Water/Ground | 50 | Surf | — |
| Qwilfish | Water/Poison | 123 | Fish | — |
| Magikarp | Water | 65 | Fish | — |
| Whismur | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Linoone | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Buizel | Water | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Bidoof | Normal | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- Rattata/Zubat/Tentacool/Tentacruel dex-less here is the routine curation-sheet cut already seen
  across the Falkner-area docs (`keep = No` in `data/generated/species_dex_meta.csv`), not a bug —
  see the memory note on this convention.
- **Type-coverage relevance (Pillar 3, Bugsy):** no Fire/Flying/Rock on this table. Flying doesn't
  need to originate here (`HACK_PLAN.md` already calls it covered from the Falkner-approach
  routes — Pidgey/Hoothoot). Fire and Rock are still open for the Bugsy audit; `HACK_PLAN.md`
  floats Growlithe as a candidate "pulled forward" Fire option but doesn't commit to where — this
  route's slots 9–12 (currently low-value Rattata/Zubat filler) are a plausible spot if Growlithe
  ends up placed pre-Azalea rather than post-Ilex Forest. Not decided; flagging for the encounter-
  rework step, not resolving it here.
- Surf/rod tables mirror the Violet City/Route 31 Tentacool-family shape rather than the
  Poliwag-family shape used on Routes 30–31 — this route is already the "brackish water" transition
  toward Union Cave's Wooper/Quagsire water tables rather than a continuation of the Violet-side
  Poliwag line. Worth keeping in mind if surf tables get normalized across the whole approach.
