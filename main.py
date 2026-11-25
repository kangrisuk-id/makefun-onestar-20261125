#!/usr/bin/env python3
"""One-Star Review of Something Essential - a make.fun entry.

The entry is a single deadpan one-star review of gravity, an everyday
essential nobody can opt out of. Running this program writes the review
to /output/entry.txt, where the competition's gate scorer reads it.

Gate contract (from the bounty kit): /output/entry.txt must be UTF-8
text of 1 to 160 characters, a single line, and not only whitespace.
"""

import os
import sys

LINE = "One star. Gravity: holds everything together but has never once caught my phone."
MAX_CHARS = 160


def validate(line: str) -> None:
    """Raise ValueError unless the line satisfies the gate contract."""
    if not line or not line.strip():
        raise ValueError("the review must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("the review must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"the review is {len(line)} characters; the gate allows at most {MAX_CHARS}"
        )
    line.encode("utf-8")  # raises UnicodeEncodeError if it cannot be UTF-8


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
