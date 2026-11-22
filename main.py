#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun entry.

Writes one short text (<=278 characters) to /output/entry.txt: a single
still image — a door inside the text itself that the reader has not
opened yet — with one twist, a note in the judge's own handwriting.
No network, no dependencies, no randomness: the same text on every run.
"""

import os

TEXT = (
    "Judge, somewhere in this text there is a door you have not opened "
    "yet. Behind it, a small room, a warm lamp, and a note in your own "
    "handwriting: 'You were looking for this.' The door is still there "
    "— and it is still waiting for you. Open it — and find out why it "
    "knows you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
