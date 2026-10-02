# Route 34

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R34_ROUTE_34` (`data/Encounters.c:2109`)
- **Map constant:** `MAP_R34` (`include/constants/maps.h:42`)
- **Connects:** Ilex Forest (south) ↔ Goldenrod City (north).
- **Leads toward:** Whitney (Goldenrod City) — this is the sole approach route (Route 32/33 feed
  Bugsy; Route 35/National Park/Route 36 feed Morty, on the far side of Goldenrod).
- **Biome Map tie-in:** `HACK_PLAN.md`'s Whitney row counter-access note: "Fighting needed
  (Normal's only weakness). Ensure Mankey or another Fighting-type is genuinely available on the
  Route 32–34 corridor before Goldenrod, not just after." Route 32/Route 33 (documented during the
  Bugsy pass) have no Fighting-type; this route is the last chance before the gym — see Notes.

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
| 1 | 20 | 10 | Miltank | Miltank | Miltank |
| 2 | 20 | 11 | Ledyba | Ledyba | Ledyba |
| 3 | 10 | 10 | Miltank | Miltank | Miltank |
| 4 | 10 | 11 | Mankey | Mankey | Mankey |
| 5 | 10 | 12 | Miltank | Miltank | Miltank |
| 6 | 10 | 12 | Miltank | Miltank | Miltank |
| 7 | 5 | 10 | Abra | Abra | Abra |
| 8 | 5 | 10 | Abra | Abra | Abra |
| 9 | 4 | 13 | Ledyba | Ledyba | Ledyba |
| 10 | 4 | 10 | Ditto | Ditto | Ditto |
| 11 | 1 | 13 | Ledyba | Ledyba | Ledyba |
| 12 | 1 | 10 | Ditto | Ditto | Ditto |

## Water/rod tables

**Surf (rate 15):** Staryu (15–25), Staryu (10–20), Starmie (15–25), Starmie (15–25), Starmie (29).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Shellder (10), Shellder (10).
**Good Rod (rate 50):** Magikarp (20), Shellder (20), Shellder (20), Corsola (20), Shellder (20).
**Super Rod (rate 75):** Shellder (40), Corsola (40), Shellder (40), Cloyster (40), Shellder (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_RALTS`, `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_STARYU`, `fishSwarm = SPECIES_MAGIKARP`.
- **Active (land):** this map is in `sSwarmMapLUT` (`src/swarms.c:23`) — the Ralts swarm fires here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Ledyba | Bug/Flying | 26 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Abra | Psychic | 72 | Walk | Morning/Day/Night |
| Ditto | Normal | 75 | Walk | Morning/Day/Night |
| Mankey | Fighting | 104 | Walk | Morning/Day/Night |
| Miltank | Normal | 112 | Walk | Morning/Day/Night |
| Staryu | Water | 125 | Surf, Swarm (surf), Fish (night) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water | 127 | Fish | — |
| Cloyster | Water/Ice | 128 | Fish | — |
| Corsola | Water/Rock | 129 | Fish | — |
| Ralts | Psychic/Fairy | 375 | Swarm (land) | — |
| Bidoof | Normal | **not in dex** | Rustling grass (Sinnoh) | — |
| Buizel | Water | **not in dex** | Rustling grass (Sinnoh) | — |
| Linoone | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Whismur | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).**
  - Water: Tentacool/Tentacruel → **Staryu/Starmie**, Krabby/Kingler → **Shellder/Cloyster** (the
    Cianwood mapping).
  - **Ralts/Kirlia/Gardevoir added to the regional dex (#375–377)**, so the active Ralts swarm is
    now a real, dex-tracked early Psychic/Fairy pickup. Gallade is left out for now; Kirlia needs a
    Dawn Stone to evolve into it.
  Earlier notes below that describe these species as dex-less or intentionally kept are superseded.
- **Resolved — Rattata replaced.** Rattata occupied slots 2/9/11 (25% of the table) while sitting
  dex-less. Replaced with **Ledyba**, already regional-dex-tracked (#26) and not spawning anywhere
  else in the build (checked both `Encounters.c` and `Headbutt.c`) — also adds real type diversity
  to a route that otherwise leans heavily Normal (Miltank ×4, Ditto ×2), and nods to Ilex Forest
  just south of here.
- Tentacool line/Krabby line/Whismur/Linoone/Buizel/Bidoof dex-less here is still the same routine
  curation-sheet cut (`keep = No`) seen throughout every other approach doc so far — left as-is.
- **Resolved — Fighting-type coverage gap closed here.** Slot 4 (10%, all-day) was originally a
  fourth Rattata slot, replaced with Mankey in an earlier pass — separate from the Rattata cleanup
  above, which covers the three slots that remained Rattata (2/9/11). This is the last route before
  Goldenrod/Whitney, so Mankey is genuinely available before the gym. No curation-sheet change was
  needed — Mankey was already regional-dex-tracked (#104).
- **Resolved — Drowzee removed from this table entirely.** Unlike the routine dex-cut fillers
  elsewhere on this route, Drowzee was flagged for outright removal rather than being left as a
  dex-less encounter. It occupied 4 of 12 slots (50% of the table — slots 1/3/5/6), so this wasn't
  a simple deletion; replaced with **Miltank**, which is already regional-dex-tracked (#112) and is
  actually vanilla Route 34's flagship wild encounter in HeartGold/SoulSilver — a strong thematic
  fit given it also foreshadows Whitney's own signature Pokémon one route later.
- `MAP_R34` being an *active* swarm map (unlike the mostly-inert swarm fields seen on the
  Falkner/Bugsy corridor) means the Ralts land swarm is a real, working alternate encounter here —
  worth remembering if a future pass wants a Psychic/Fairy pickup on this route without touching
  the base table.
- This route's Fighting gap mirrors Bugsy's Fire gap almost exactly: a single dex-cut, contributing-
  nothing filler species (there, Spearow; here, Rattata) on the last pre-gym route is the natural
  replacement slot.
