#!/usr/bin/env python3
"""One Word, First Thought: emit the chosen word to /output/entry.txt.

The pick is Defenestration: the act of throwing something out of a window.
Surprising on arrival, vivid in one image, funny in its sound, and the kind
of word nobody reaches for by default. Stdlib only, deterministic, no
network. The output directory is created if needed but never removed; only
entry.txt is written inside it.
"""

from pathlib import Path

WORD = "Defenestration"

OUT_PATH = Path("/output") / "entry.txt"


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
