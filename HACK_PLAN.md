# Hack Plan (working doc)

Working title: **Pokémon Vibrant Gold**

This is the living design doc for the ROM hack built on this hg-engine fork. Update it as
decisions get made — treat stale/contradicted sections as wrong and fix them rather than leaving
both versions around.

## Vision

**Pokémon Vibrant Gold** — a "vibrant Johto": the region's biomes are made more ecologically
real and varied, Fairy type exists as part of the world (not just bolted onto move/type charts),
and every gym leader, rival, and the Elite Four are rebuilt as genuinely skilled "ace trainers"
running real team archetypes (hazards, weather, trick room, priority cores, etc.) — not just
"same 2-3 mons at a higher level." Their rosters and the wild encounter pool around them are
grounded in their local biome, so the world reads as more alive. Regular trainers get a
difficulty/competency pass too, but the gym/rival/E4 tier is the showcase.

Note: the physical/special move split is **already baseline HeartGold/Gen 4 behavior** (Gen 4
introduced per-move categorization, not per-type) — it's not an hg-engine addition or something
this hack needs to implement. hg-engine's relevant contribution here is keeping move
*categorization itself* up to date with later-generation reclassifications (e.g. moves that
became physical/special in Gen 6+) as part of its broader "updated move effects" work.

Scope for v1: **no new or altered maps.** All changes are to trainer data, dex curation,
encounters, movesets/items, and light dialogue/flavor text. Map edits (retheming a route's
encounter table to match its biome more visibly, or eventually new areas) are an explicit
possible v2+ branch, not a v1 blocker.

## Phased approach

This is explicitly a multi-phase project and also a learning exercise (first real hands-on pass
with hg-engine/ROM hacking tooling for the person building it). Phases run in order, each one
building on the last rather than in parallel:

1. **Phase 1 — Johto rework.** Everything in this doc (biome map, dex curation, gym/rival/E4
   rebuild, trainer competency pass, QoL) scoped to Johto only. This is the current focus and
   where the Milestones section below applies.
2. **Phase 2 — Kanto post-game.** Once Johto is done and playtested, give Kanto's post-game gyms
   (and any E4 rematch content) the same archetype/biome/type-coverage treatment. Deferred until
   Phase 1 is solid — not started in parallel, since Phase 1 is also where the workflow/tooling
   gets learned.
3. **Phase 3 — New story.** With the biomes, gym leaders, and dex refreshed across both regions,
   layer a new story on top of that refreshed world (new narrative beats, not just flavor text —
   this goes beyond Pillar 6's "light narrative flavor" scope for v1). Not scoped in detail yet;
   revisit once Phase 2 is complete.

## Pillars

1. **Ace-trainer gym/rival/E4 rebuilds** — real archetypes, biome-appropriate rosters, movesets
   and items that support the archetype (not just STAB spam).
2. **Biome-grounded, curated dex** — trim the "everything through Gen 9" default roster down to
   what fits each area's ecology; support this through the game's actual Regional Dex vs
   National Dex mechanism (see Technical Approach) rather than deleting species data.
3. **Progression-aware type coverage** — biome realism is subordinate to fairness: the player
   must always have a plausible, catchable (or otherwise reasonably obtainable — TM/tutor/starter
   movepool count) counter-type path into the *next* gym before reaching it. If a gym leader's
   home biome doesn't naturally contain those counters, the counter-types get placed on the
   route(s) leading into that gym rather than forcing an ecologically-wrong mon into the gym's
   own biome. See Technical Approach for how this gets checked per gym.
4. **Trainer competency pass (non-gym)** — route/gym-adjacent trainers get better flag
   configurations (`aiFlags` in `data/Trainers.c`) and less thrown-together teams, scaled below
   the gym/rival/E4 tier.
5. **QoL modernization** — lean on existing `CONFIG.md` toggles (reusable TMs, deletable HMs,
   EV/IV viewer, reusable repels, capture experience, critical captures, etc.) rather than
   building new QoL systems from scratch.
6. **Light narrative flavor** — dialogue/flavor text leans into "ace trainers defending their
   biome/region" framing; no new story beats or characters planned for v1.

## Technical approach (mapped to this repo)

- **Dex curation** → `data/RegionalDex.c` (+ `data/PokedexArea.c`, `data/PokedexSort.c` for
  area/sort-list consistency). Curate via the *regional* dex list, keep full species data intact
  so National Dex / `ALWAYS_HAVE_NATIONAL_DEX` (see `CONFIG.md`) still works for completionists
  post-game. Don't strip entries from `data/Species.c` — curation is about what's *reachable and
  dex-tracked by default*, not deleting content.
- **Encounters** → `data/Encounters.c` (routes/caves/etc.) and `data/SafariEncounters.c`. This is
  the lever for "this route's wild mons match its biome and match what the local gym leader uses."
- **Type coverage audit** → for each gym, before finalizing its roster: list the gym's types,
  compute the standard SE-against-it type set, then check the cumulative catchable/obtainable
  pool up to and including the route(s) just before that gym (wild encounters via
  `data/Encounters.c`, static/gift mons, TM/tutor moves available by that point, and starter
  movepools from `data/learnsets/`) actually contains at least one reasonable counter option.
  **Preference order: wild-caught first.** Default to satisfying coverage with a wild-encounterable
  species; fall back to TM/tutor-onto-an-off-type-mon or starter-movepool coverage only when a
  wild option genuinely doesn't fit the biome/route. This is a soft preference, not a hard gate —
  don't force an ecologically-wrong species into a route just to check the box when a TM/tutor
  fallback reads more naturally.
  Where the gym's own biome can't supply it without breaking ecological plausibility, place the
  counter on an approach route instead of forcing a mismatched species into the gym's biome.
  This audit should be re-run whenever a gym's typing/archetype or a route's encounter table
  changes — it's a checklist step in milestones 2–3 below, not a one-time pass.
- **Gym/rival/E4/trainer rosters** → `data/Trainers.c` (`sTrainerData[]`), typed via
  `include/trainer_data.h`. This is where team archetype, `aiFlags`, IVs/EVs, items, ability
  slots, and ball seals all get set per trainer.
- **AI tuning** → `aiFlags` bitfield on each trainer (`F_PRIORITIZE_SUPER_EFFECTIVE`,
  `F_EVALUATE_ATTACKS`, `F_EXPERT_ATTACKS`, `F_PRIORITIZE_STATUS_MOVES`, `F_RISKY_ATTACKS`,
  `F_PRIORITIZE_DAMAGE`, `F_PRIORITIZE_HEALING`, `F_USE_WEATHER`, etc. — full list in
  `include/trainer_data.h`). `F_TRAINER_EXPERT_AI` is a pre-built "best available" combo. This is
  the ceiling for how smart a given fight can play without engine-level AI work.
- **Movesets/abilities/items** → `data/Species.c` (base stats/abilities/types are shared —
  changes here affect every user of that species, so be careful about ripple effects into wild
  encounters and other trainers) and `data/learnsets/` for level-up/TM/egg moves. Battle-mechanic
  correctness for any custom move/ability behavior goes through `data/battle_scripts/` and should
  get a test in `data/battle_tests/`.
- **QoL** → toggle flags in `armips/include/config.s` / `include/config.h` per `CONFIG.md`.

## Reality check: what "smarter AI" actually means here

hg-engine's trainer AI is the original Gen 3/4-era flag-based system (see `src/battle/ai.c`,
`armips/asm/trainer_ai.s`) — a from-scratch AI rewrite is listed as unstarted, long-term upstream
work, not something this hack should plan to build itself. Practical levers we actually have:
- Set aggressive flag combos (`F_TRAINER_EXPERT_AI` and friends) on ace-tier trainers.
- Build teams that are *hard to play against* by construction (coverage, synergy, held items,
  speed control) rather than relying on the AI to outplay the player.
- Watch upstream for AI-related fixes/improvements when merging `upstream/main`.

## Open decisions (fill in as we go)

- [ ] Working title for the hack.
- [x] Biome map (Johto) — **Johto gyms + E4 + Champion + Silver drafted**, see Biome Map section
      below. Kanto post-game gyms are explicitly **deferred to Phase 2** (see Phased approach
      above), not part of this pass.
- [ ] Regional dex size/target — how curated is "curated"? (e.g. Kanto/Johto-plausible species
      only, vs. a stricter per-biome cap.)
- [ ] Which `CONFIG.md` toggles are in/out for v1 (draft a concrete list rather than "most of
      them").
- [ ] How far the "trainer competency pass" extends below gym/rival/E4 tier (every route trainer?
      just gym-adjacent ones? Elite Four rematch/post-game trainers?).
- [x] Mega Evolution / Primal Reversion / Fairy type / Hidden Abilities — **resolved: all
      enabled.** Fairy type is core to the "vibrant Johto" vision (not just inherited default).
      Mega Evolution stays on as a showcase moment for ace-trainer fights (gym leaders/rivals/
      champion). Hidden Abilities stay on for build diversity on both player and trainer rosters.
- [ ] Any species exclusions/inclusions driven by story tone rather than biome (legendaries,
      pseudo-legendaries, event mons).
- [x] How strict "obtainable" counts for the type-coverage audit — **resolved:** prefer
      wild-caught coverage by default, but it's a soft preference, not a hard rule. TM/tutor
      moves onto an off-type mon or a starter's own movepool can satisfy the audit when a wild
      option doesn't fit the biome/route naturally.

## Biome Map (Phase 1 — Johto; Kanto post-game gyms/E4 rematch are Phase 2, see Phased approach)

Draft pairing of type/archetype/biome for each Johto gym, the Elite Four, Champion, and rival
Silver. Each entry includes the type-coverage note per Pillar 3 — what the player needs access to
on the way in, and where that plausibly comes from.

| Trainer | Type | Archetype | Biome rationale | Counter-access note |
|---|---|---|---|---|
| **Falkner** (Violet City) | Flying | Speed-control hit-and-run (Tailwind/priority support around fast bird sweepers) | Violet sits at the forest/cliff edge of Route 30–32; birds (Pidgey/Hoothoot line) already fit this transition zone | Rock/Electric/Ice needed. Rock via Geodude (Dark Cave/Route 31, already vanilla-natural). Consider pulling Mareep earlier onto Route 32's farmland edge for an Electric option too — fits pastoral biome and gives a second counter path. |
| **Bugsy** (Azalea Town) | Bug | Hazard-setting swarm (Sticky Web/Spikes support into paralysis-inducing attackers) | Ilex Forest is already a deep-forest biome — canon-correct, just deepen bug variety (Scyther/Pinsir via Headbutt trees) | Fire/Flying/Rock needed. Flying already covered from Falkner-approach routes. Consider an earlier Fire option (e.g. Growlithe pulled forward) so Fire isn't first available much later. |
| **Whitney** (Goldenrod City) | Normal | Bulky pivot / status-stall around a hard-hitting wallbreaker (keep Miltank as the signature threat, build real support around it) | Goldenrod's surrounding farmland (Route 34 / National Park edge) fits Normal-type livestock/common-critter ecology well already | Fighting needed (Normal's only weakness). Ensure Mankey or another Fighting-type is genuinely available on the Route 32–34 corridor before Goldenrod, not just after. |
| **Morty** (Ecruteak City) | Ghost | Trick Room / status-stall (Will-O-Wisp burn stall, trapping) | Burned Tower / old-town lore is already a strong ghost biome, no change needed | Dark needed (Ghost's other weakness besides Ghost itself). Murkrow (Dark/Flying) already spawns near National Park at night in vanilla — confirm it's reachable *before* Ecruteak, not after. |
| **Chuck** (Cianwood City) | Fighting | Bulky rain-abuse (Rain Dance + Swift Swim, keep Poliwrath as signature) | Cianwood is a stormy coastal island reached by Surf — genuinely fits a rain/ocean archetype | Flying/Psychic/Fairy needed. Flying already covered (Zubat/Golbat on the water route). Fairy is a good fit here too — Jigglypuff/Igglybuff already spawn on the Route 47/48 approach; confirm availability before Cianwood. |
| **Jasmine** (Olivine City) | Steel | Defensive wall core (Toxic/Protect stall, Steelix as signature) | Olivine's port/lighthouse industrial setting fits Steel ecology well already | Fire/Fighting/Ground needed (post-Fairy Steel weaknesses). All three should already be available via earlier additions (Growlithe, Machop/Mankey, Sandshrew/Geodude) — verify during the audit rather than assume. |
| **Pryce** (Mahogany Town) | Ice | Hail support / bulky ice wall (Piloswine/Slush Rush as signature) | Ice Path / Lake of Rage area is a genuinely icy mountain biome already | Fire/Fighting/Rock/Steel — Ice has many weaknesses, should be well-covered by this point; still worth the audit pass. |
| **Clair** (Blackthorn City) | Dragon | Dragon Dance power core with priority backup (Kingdra as signature) | Blackthorn / Dragon's Den is mountain-and-dragon-lore biome already, canon-correct | Ice/Dragon/Fairy needed. Fairy is a nice callback here too — Snubbull/Granbull (now Fairy-type) fit a wilder mountain-forest approach; consider placing them on a pre-Blackthorn route. |
| **Elite Four: Will** | Psychic | Bulky special core with Calm Mind setup | Indoor/Indigo Plateau — no strong biome tie, character-driven instead | Dark/Ghost/Bug needed — post-game roster should already have full access. |
| **Elite Four: Koga** | Poison | Trapping/hazard stall (Toxic Spikes, Sludge Bomb spread, screens) | Indoor — character-driven (ninja/poison theme carries over from Fuchsia lore) | Ground/Psychic needed — should be well covered post-game. |
| **Elite Four: Bruno** | Fighting | Physical power core, priority + setup sweepers | Indoor — character-driven | Flying/Psychic/Fairy needed — Fairy again relevant at this tier. |
| **Elite Four: Karen** | Dark | Mixed-attacker core exploiting Psychic/Ghost, pressure via intimidation | Indoor — character-driven | Fighting/Bug/Fairy needed. |
| **Champion: Lance** | Dragon | Apex Dragon Dance/power core, likely holds the hack's showcase Mega | Indigo Plateau — character-driven, dragon mastery as narrative capstone | Ice/Dragon/Fairy — final check that the player's built-up team actually has answers here. |
| **Rival: Silver** | Mixed (evolves through the game; leans Dark/aggressive-tempo) | Aggressive, adapts to counter the player's starter each encounter — the "rival pressure" archetype rather than a fixed type identity | Not biome-tied — follows the player's route, appears at multiple points (New Bark, Cherrygrove, Azalea, Burned Tower, Radio Tower, Victory Road, etc.) | N/A — Silver's role is to pressure-test the player's current team, not gate progress the way a gym does. |

**Note on Fairy type placement**: Fairy shows up meaningfully at three points above (Chuck/Cianwood
approach, Clair/Blackthorn approach, and Bruno/Karen at E4 tier) rather than being clustered in
one area — keeps it feeling woven into the world rather than bolted on as a single "fairy zone."

## Milestones — Phase 1 (Johto)

Kanto post-game (Phase 2) and the new story (Phase 3) get their own milestone lists once each
phase starts — not drafted yet, see Phased approach above.

1. **Foundation**: confirm `CONFIG.md` toggle list for v1; get a clean baseline `test.nds`
   building from current `main`.
2. **Biome map**: draft the gym-leader/area/archetype/biome mapping — done, see Biome Map above.
   Run the type-coverage audit per gym as part of this pass, not after — it can change which
   route gets which encounters.
3. **Dex curation pass**: implement regional dex per the biome map via `data/RegionalDex.c` +
   encounter table alignment in `data/Encounters.c`, re-checking the type-coverage audit as
   encounter tables get finalized.
4. **Gym/rival/E4 rebuild**: rebuild rosters in `data/Trainers.c` per the biome/archetype map,
   iterating with playtesting (use `data/battle_tests/` for mechanic-level checks, manual
   playtesting in an emulator for feel). Re-run the coverage audit if a gym's final archetype
   shifts its effective typing (e.g. a mixed-type archetype changes what actually threatens it).
5. **Trainer competency pass**: extend improved flag configs/team quality to non-gym trainers.
6. **Polish**: flavor text/dialogue pass, QoL verification, full playthrough test.
