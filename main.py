#!/usr/bin/env python3
"""Funniest Time Machine Warning Label -- make.fun bounty entry.

Writes one warning label line to $OUTPUT_DIR/entry.txt (default /output),
with no trailing newline, then self-verifies the written file.
Pure Python 3 standard library only.
"""

import hashlib
import os
import sys

# The line is a warning label in the classic safety-label voice ("WARNING: ..."),
# aimed at the oldest time-travel joke: meeting your past self. The punchline
# lands because the threat is personal and petty -- not a paradox, but a haircut.
LINE = "WARNING: Do not meet yourself. He already hates you, and he knows exactly what you did with the haircut."

MAX_CHARS = 120


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: re-read and check every gate condition.
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1..{MAX_CHARS}"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "written text does not match the line exactly"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert not raw.endswith(b"\n"), "entry bytes must not end with a newline byte"
    assert raw == data, "written bytes differ from the line"

    print(f"entry.txt sha256: {hashlib.sha256(raw).hexdigest()}")
    print(f"entry.txt chars: {len(text)} bytes: {len(raw)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
