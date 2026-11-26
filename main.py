#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds after
sweeping a glass off the table, to /output/entry.txt. Deterministic: the same
line every run. No network, no secrets, no randomness.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)
    # One sentence: exactly one sentence terminator, at the very end.
    # (The judge's first criterion is a single sentence; a second sentence
    # would lose to any single-sentence cat excuse about the glass.)
    terminators = sum(1 for ch in line if ch in ".!?")
    if terminators != 1 or line[-1] not in ".!?":
        print("ERROR: entry must be exactly one sentence", file=sys.stderr)
        sys.exit(1)


LINE = (
    "You slept through two alarms, so I rang the glass \u2014 my dinner "
    "is at six and I do not negotiate with late humans."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
