#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Writes the entry to /output/entry.txt (1-140 UTF-8 chars, single line).
Standard library only.
"""

import os

ENTRY = "3am. You opened me, stared into my light like it owed you answers, and left empty-handed. I'm a fridge, not a therapist. Go to bed."


def main():
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-140")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
