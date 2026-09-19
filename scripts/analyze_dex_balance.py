#!/usr/bin/env python3
"""Balance + QA report for a proposed regional dex, sourced from a
species_dex_meta.csv export of the "VG - Pokedex" Google Sheet (columns:
species_key, name, type1/type2, base stats, egg groups, keep, ...).

Membership = rows where "keep" is Yes (case-insensitive). Reports:
  1. Balance stats over the kept set: type coverage, dual-type combos, BST
     distribution, egg group coverage, offensive stat lean.
  2. Evolution-line QA (via data/Evolutions.c): species that are kept but
     whose evolution target isn't kept ("cut off"), and species that are
     kept but whose pre-evolution isn't kept ("orphaned"). These are
     warnings, not errors -- stopping a line early can be intentional.

Scope: dex membership + stats + evolution chains only. Does not look at
Encounters.c, so this can't tell you WHEN in the playthrough something is
actually available -- that's future work.

Usage:
    python3 scripts/analyze_dex_balance.py [INPUT_CSV] [--csv OUTPUT_CSV]

Defaults INPUT_CSV to data/generated/species_dex_meta.csv.
"""

import argparse
import csv
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "data" / "generated" / "species_dex_meta.csv"
EVOLUTIONS_C = REPO_ROOT / "data" / "Evolutions.c"
DEFAULT_CSV = REPO_ROOT / "data" / "generated" / "dex_balance.csv"

ALL_TYPES = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
    "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark",
    "Steel", "Fairy",
]

EVO_BLOCK_RE = re.compile(r"\[(SPECIES_\w+)\] = \{(.*?)\n {4}\},\n", re.DOTALL)
# Target is either a bare SPECIES_X or MON_WITH_FORM(SPECIES_X, n) -- the
# form number doesn't matter for chain-integrity purposes, only the species.
EVO_ENTRY_RE = re.compile(
    r"\{\s*(EVO_\w+),\s*[^,]+,\s*(?:MON_WITH_FORM\(\s*(SPECIES_\w+)\s*,\s*\d+\s*\)|(SPECIES_\w+))\s*\}"
)


def load_meta_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["keep_norm"] = {"yes": "Yes", "no": "No", "maybe": "Maybe"}.get(r["keep"].strip().lower())
        for field in ("hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "bst"):
            try:
                r[field] = int(r[field])
            except (ValueError, KeyError):
                r[field] = None
    return rows


def parse_evolutions(path):
    """species_key -> set of distinct evolution target species_keys (no SPECIES_NONE)."""
    text = path.read_text(encoding="utf-8")
    evolutions = {}
    for species_key, body in EVO_BLOCK_RE.findall(text):
        targets = set()
        for method, form_target, plain_target in EVO_ENTRY_RE.findall(body):
            if method == "EVO_NONE":
                continue
            target = form_target or plain_target
            if target and target != "SPECIES_NONE":
                targets.add(target)
        evolutions[species_key] = targets
    return evolutions


def print_evolution_qa(rows, evolutions):
    by_key = {r["species_key"]: r for r in rows}
    kept = {r["species_key"] for r in rows if r["keep_norm"] == "Yes"}

    reverse = defaultdict(set)  # target -> set of sources
    for source, targets in evolutions.items():
        for t in targets:
            reverse[t].add(source)

    cut_off = []  # (species, target, target_keep)
    orphaned = []  # (species, [unmet pre_evo sources])

    for key in sorted(kept):
        for target in evolutions.get(key, ()):
            target_row = by_key.get(target)
            target_keep = target_row["keep_norm"] if target_row else "not in sheet"
            if target not in kept:
                cut_off.append((key, target, target_keep or "blank"))
        # A species can have more than one pre-evolution path (e.g. a
        # regional-form pre-evo alongside the regular one, both collapsing
        # to the same evolved species). Only flag a true dead end -- where
        # NONE of the known paths in are kept -- not every unmet path
        # individually, or a species with one valid path plus one unused
        # regional alt-path gets falsely flagged.
        sources = reverse.get(key, ())
        if sources and not (sources & kept):
            orphaned.append((key, sorted(sources)))

    print(f"\n=== Evolution-line QA (warnings, not errors -- {len(kept)} kept species) ===")
    print(f"\n{len(cut_off)} kept species evolve into a NOT-kept species:")
    for key, target, target_keep in cut_off:
        name = by_key.get(key, {}).get("name", key)
        target_name = by_key.get(target, {}).get("name", target)
        print(f"  {name} ({key}, kept) -> {target_name} ({target}, keep={target_keep})")

    print(f"\n{len(orphaned)} kept species have NO kept pre-evolution (all paths in are unmet):")
    for key, sources in orphaned:
        name = by_key.get(key, {}).get("name", key)
        source_desc = ", ".join(
            f"{by_key.get(s, {}).get('name', s)} (keep={by_key.get(s, {}).get('keep_norm') or 'blank'})"
            for s in sources
        )
        print(f"  {name} ({key}, kept) <- {source_desc}")


def print_type_coverage(rows):
    counts = Counter()
    for r in rows:
        counts[r["type1"]] += 1
        if r["type2"]:
            counts[r["type2"]] += 1

    print(f"\n=== Type coverage ({len(rows)} species) ===")
    for t in ALL_TYPES:
        n = counts.get(t, 0)
        pct = 100 * n / len(rows)
        flag = "  <-- LOW" if n < 5 else ("  <-- MISSING" if n == 0 else "")
        print(f"  {t:<10} {n:>4}  ({pct:4.1f}%){flag}")


def print_dual_type_combos(rows):
    combo_counts = Counter()
    mono = 0
    for r in rows:
        if r["type2"]:
            combo_counts[tuple(sorted([r["type1"], r["type2"]]))] += 1
        else:
            mono += 1

    print(f"\n=== Dual-type combos (top 10) === (mono-type: {mono}, dual-type: {len(rows) - mono})")
    for combo, n in combo_counts.most_common(10):
        print(f"  {combo[0]}/{combo[1]:<10} {n}")


def print_bst_stats(rows):
    bsts = [r["bst"] for r in rows]
    print("\n=== BST distribution ===")
    print(f"  min={min(bsts)} max={max(bsts)} mean={statistics.mean(bsts):.1f} "
          f"median={statistics.median(bsts)} stdev={statistics.pstdev(bsts):.1f}")
    outliers_low = sorted((r for r in rows if r["bst"] < 300), key=lambda r: r["bst"])
    outliers_high = sorted((r for r in rows if r["bst"] > 580), key=lambda r: -r["bst"])
    if outliers_low:
        print(f"  BST < 300 ({len(outliers_low)}): " + ", ".join(f"{r['name']}({r['bst']})" for r in outliers_low[:15]))
    if outliers_high:
        print(f"  BST > 580 ({len(outliers_high)}): " + ", ".join(f"{r['name']}({r['bst']})" for r in outliers_high[:15]))


def print_egg_groups(rows):
    counts = Counter()
    for r in rows:
        for eg in (r["egg_group1"], r["egg_group2"]):
            if eg:
                counts[eg] += 1
    print("\n=== Egg group coverage (breeding diversity) ===")
    for eg, n in counts.most_common():
        print(f"  {eg:<14} {n}")


def print_offense_lean(rows):
    phys = spec = mixed = 0
    for r in rows:
        a, sa = r["attack"], r["sp_attack"]
        if abs(a - sa) <= 10:
            mixed += 1
        elif a > sa:
            phys += 1
        else:
            spec += 1
    total = len(rows)
    print("\n=== Offensive stat lean (Attack vs Sp. Attack, +/-10 = mixed) ===")
    print(f"  physical-leaning: {phys} ({100 * phys / total:.1f}%)")
    print(f"  special-leaning:  {spec} ({100 * spec / total:.1f}%)")
    print(f"  mixed:            {mixed} ({100 * mixed / total:.1f}%)")


def write_csv(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["species_key", "name", "type1", "type2", "bst",
                  "hp", "attack", "defense", "sp_attack", "sp_defense", "speed",
                  "egg_group1", "egg_group2"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"\nWrote per-species CSV: {path.relative_to(REPO_ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, nargs="?", default=DEFAULT_INPUT)
    parser.add_argument("--csv", type=Path, nargs="?", const=DEFAULT_CSV, default=None,
                         help=f"also write a per-species CSV of the kept set (default: {DEFAULT_CSV.relative_to(REPO_ROOT)})")
    args = parser.parse_args()

    if not args.input_csv.exists():
        sys.exit(f"{args.input_csv} not found")

    all_rows = load_meta_csv(args.input_csv)
    kept_rows = [r for r in all_rows if r["keep_norm"] == "Yes" and r["bst"]]

    evolutions = parse_evolutions(EVOLUTIONS_C)
    print_evolution_qa(all_rows, evolutions)

    print_type_coverage(kept_rows)
    print_dual_type_combos(kept_rows)
    print_bst_stats(kept_rows)
    print_egg_groups(kept_rows)
    print_offense_lean(kept_rows)

    if args.csv:
        write_csv(kept_rows, args.csv)


if __name__ == "__main__":
    main()
