"""Write a single word to the output file."""

import os
import sys

WORD = "Defenestration"

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def main():
    if not WORD or " " in WORD:
        sys.exit("error: entry must be a single non-empty word")
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
