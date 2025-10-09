#!/usr/bin/env python3
"""
mutator.py - chained wordlist mutator

Example:
  ./mutator.py -w list.txt -o out.txt -a 2023 2024 2025! -H
  ./mutator.py -w list.txt -o out.txt -H1
  ./mutator.py -w list.txt -o out.txt -L2
  ./mutator.py -w list.txt -o out.txt -All
"""

import argparse
import sys
from pathlib import Path


def mutate_word(
    word,
    append_list=None,
    prepend_list=None,
    higher=False,
    lower=False,
    capitalize=False,
    reverse=False,
    higher_first=False,
    lower_first=False,
    all_case=False
):
    """Apply all requested transformations and return list of results"""
    results = []
    prepend_list = prepend_list or [""]
    append_list = append_list or [""]

    for pre in prepend_list:
        for app in append_list:
            w = f"{pre}{word}{app}"

            # Apply case transformations
            if higher:
                w = w.upper()
            elif lower:
                w = w.lower()
            elif capitalize:
                w = w.capitalize()
            elif higher_first:
                if w:
                    w = w[0].upper() + w[1:]
            elif lower_first:
                if w:
                    w = w[0].lower() + w[1:]
            elif all_case:
                # Generate both versions: capitalized and lowercase-first
                if w:
                    capitalized = w[0].upper() + w[1:]
                    lower_first_v = w[0].lower() + w[1:]
                    results.extend([capitalized, lower_first_v])
                    continue  # skip appending again below

            # Reverse if required
            if reverse:
                w = w[::-1]

            results.append(w)
    return results


def parse_args():
    p = argparse.ArgumentParser(description="Wordlist mutator: chained append/prepend + case transforms")
    p.add_argument("-w", "--wordlist", required=True, help="Input wordlist file (one word per line)")
    p.add_argument("-o", "--output", required=True, help="Output file to write results")
    p.add_argument("-a", "--append", nargs="*", help="Append one or more strings (e.g. -a 2023 2024 2025!)")
    p.add_argument("-p", "--prepend", nargs="*", help="Prepend one or more strings (e.g. -p admin root user-)")

    # Case control flags
    p.add_argument("-H", "--highercase", action="store_true", dest="higher", help="Convert to UPPERCASE")
    p.add_argument("-L", "--lowercase", action="store_true", dest="lower", help="Convert to lowercase")
    p.add_argument("-C", "--capitalize", action="store_true", dest="capitalize", help="Capitalize each word")
    p.add_argument("-H1", "--higher-first", action="store_true", dest="higher_first", help="Uppercase only first letter")
    p.add_argument("-L2", "--lower-first", action="store_true", dest="lower_first", help="Lowercase only first letter")
    p.add_argument("-All", "--all-case", action="store_true", dest="all_case",
                   help="Generate both variants (Uppercase first letter and Lowercase first letter)")

    p.add_argument("-r", "--reverse", action="store_true", dest="reverse", help="Reverse each word")
    return p.parse_args()


def main():
    args = parse_args()
    in_path = Path(args.wordlist)
    out_path = Path(args.output)

    if not in_path.exists():
        print(f"[!] Input file not found: {in_path}", file=sys.stderr)
        sys.exit(2)

    with in_path.open("r", encoding="utf-8", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    mutated = []
    for word in words:
        mutated.extend(
            mutate_word(
                word,
                append_list=args.append,
                prepend_list=args.prepend,
                higher=args.higher,
                lower=args.lower,
                capitalize=args.capitalize,
                reverse=args.reverse,
                higher_first=args.higher_first,
                lower_first=args.lower_first,
                all_case=args.all_case,
            )
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for m in mutated:
            f.write(m + "\n")

    print(f"[+] Generated {len(mutated)} mutated words to {out_path}")


if __name__ == "__main__":
    main()
