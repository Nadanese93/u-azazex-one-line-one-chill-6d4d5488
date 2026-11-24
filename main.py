#!/usr/bin/env python3
"""One Line, One Chill — a single-sentence horror line, under 200 characters.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

ENTRY = "The self-checkout thanked me by name, and I have never typed it in, because this store closed six years ago."
MAX_CHARS = 200


def main():
    if not ENTRY.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} gate")
    if sum(ENTRY.count(c) for c in ".!?") != 1:
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
