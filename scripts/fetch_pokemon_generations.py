#!/usr/bin/env python3
"""Look up each species' introduction generation via PokeAPI (pokelance) and
fill it into a "Generation" column of a dex-curation CSV exported from the
"VG - Pokedex" Google Sheet.

The engine's SPECIES_ constant values are NOT national dex numbers beyond
Gen 4 (e.g. SPECIES_VICTINI == 544, not its real dex number 494) -- extra
enum slots are reserved for forms/EGG/etc. throughout the range. So instead
of resolving IDs, this script:

  1. Builds species_key -> display name from the input CSV itself.
  2. Loads data/FormToSpeciesMapping.c to map form species (Mega/regional/
     Gigantamax/etc.) back to their base species key.
  3. Slugifies the (base) display name into a PokeAPI identifier and calls
     GET /pokemon-species/{slug} to read its `generation`.

Usage:
    python3 scripts/fetch_pokemon_generations.py INPUT_CSV [-o OUTPUT_CSV]

INPUT_CSV must have "species_key", "name", and "Generation" columns (as
exported from the VG - Pokedex sheet). Defaults OUTPUT_CSV to
data/generated/vg_pokedex_with_generations.csv (gitignored). Also prints a
newline-separated "Generation" column (in input row order) to
data/generated/vg_pokedex_generation_column.txt, ready to paste into column T
of the sheet -- this script cannot write to Google Sheets directly.
"""

import argparse
import asyncio
import csv
import re
import sys
import unicodedata
from pathlib import Path

import pokelance
from pokelance.exceptions import HTTPException

REPO_ROOT = Path(__file__).resolve().parent.parent
FORM_MAPPING_C = REPO_ROOT / "data" / "FormToSpeciesMapping.c"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "generated" / "vg_pokedex_with_generations.csv"
DEFAULT_COLUMN_OUTPUT = REPO_ROOT / "data" / "generated" / "vg_pokedex_generation_column.txt"

FORM_MAPPING_RE = re.compile(r"\[(SPECIES_\w+)\s*-\s*SPECIES_\w+\]\s*=\s*(SPECIES_\w+),")

GENERATION_TO_INT = {f"generation-{roman}": n for n, roman in enumerate(
    ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"], start=1
)}

# Names that don't slugify cleanly with the generic rules below.
SLUG_OVERRIDES = {
    "nidoran♀": "nidoran-f",
    "nidoran♂": "nidoran-m",
    "farfetch'd": "farfetchd",
    "sirfetch'd": "sirfetchd",
    "mr. mime": "mr-mime",
    "mr. rime": "mr-rime",
    "mime jr.": "mime-jr",
    "type: null": "type-null",
    "flabébé": "flabebe",
}


def load_form_to_base(path):
    form_to_base = {}
    for form_key, base_key in FORM_MAPPING_RE.findall(path.read_text(encoding="utf-8")):
        form_to_base[form_key] = base_key
    return form_to_base


def resolve_base_key(species_key, form_to_base, max_depth=5):
    key = species_key
    for _ in range(max_depth):
        base = form_to_base.get(key)
        if base is None or base == key:
            return key
        key = base
    return key


def slugify_name(name):
    lowered = name.strip().lower()
    if lowered in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[lowered]
    normalized = unicodedata.normalize("NFKD", lowered)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_only = ascii_only.replace("'", "")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_only).strip("-")
    return slug


def slugify_species_key(species_key):
    # SPECIES_ constant identifiers preserve the full/real name (no display
    # truncation, no hack-specific flavor renames), and are already close to
    # kebab-case -- e.g. SPECIES_IRON_TREADS -> "iron-treads",
    # SPECIES_NIDORAN_F -> "nidoran-f", SPECIES_MR_MIME -> "mr-mime".
    body = species_key[len("SPECIES_"):] if species_key.startswith("SPECIES_") else species_key
    return body.lower().replace("_", "-")


async def fetch_species(client, slug, cache):
    if slug in cache:
        return cache[slug]
    try:
        species = await client.pokemon.fetch_pokemon_species(slug)
    except HTTPException:
        cache[slug] = None
        return None
    generation = GENERATION_TO_INT.get(species.generation.name)
    cache[slug] = generation
    return generation


async def fetch_generation(client, species_key, display_name, cache):
    # Try the constant-derived slug first (matches PokeAPI almost exactly
    # and isn't subject to the 10-char display-name truncation this engine
    # applies to in-game species names), then fall back to the sheet's
    # display name for anything that still doesn't resolve.
    for slug in (slugify_species_key(species_key), slugify_name(display_name)):
        generation = await fetch_species(client, slug, cache)
        if generation is not None:
            return generation
    return None


async def resolve_all(rows, form_to_base, concurrency=8):
    name_by_key = {row["species_key"]: row["name"] for row in rows}
    cache = {}
    unresolved = []
    sem = asyncio.Semaphore(concurrency)

    async with pokelance.PokeLance() as client:
        async def resolve_row(row):
            key = row["species_key"]
            if key == "SPECIES_NONE" or not row["name"].strip():
                return row, None
            base_key = resolve_base_key(key, form_to_base)
            base_name = name_by_key.get(base_key, row["name"])
            async with sem:
                generation = await fetch_generation(client, base_key, base_name, cache)
            if generation is None:
                unresolved.append((key, row["name"], base_key, slugify_species_key(base_key)))
            return row, generation

        results = await asyncio.gather(*(resolve_row(row) for row in rows))

    return results, unresolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, help="CSV exported from the VG - Pokedex sheet")
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--column-output", type=Path, default=DEFAULT_COLUMN_OUTPUT)
    args = parser.parse_args()

    with args.input_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if "Generation" not in fieldnames:
        sys.exit("Input CSV has no 'Generation' column")

    form_to_base = load_form_to_base(FORM_MAPPING_C)
    results, unresolved = asyncio.run(resolve_all(rows, form_to_base))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row, generation in results:
            row["Generation"] = "" if generation is None else str(generation)
            writer.writerow(row)

    with args.column_output.open("w", encoding="utf-8") as f:
        for row, generation in results:
            f.write(("" if generation is None else str(generation)) + "\n")

    resolved_count = sum(1 for _, g in results if g is not None)
    print(f"Resolved {resolved_count}/{len(rows)} rows.")
    print(f"Full CSV: {args.output.relative_to(REPO_ROOT)}")
    print(f"Paste-ready column (row order preserved): {args.column_output.relative_to(REPO_ROOT)}")

    if unresolved:
        print(f"\n{len(unresolved)} unresolved:")
        for key, name, base_key, slug in unresolved:
            print(f"  {key} ({name!r}) -> base={base_key} slug={slug!r}")


if __name__ == "__main__":
    main()
