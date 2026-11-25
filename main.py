#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note (make.fun entry).

Writes the keeper patch-note line byte-exact to /output/entry.txt.
Pure stdlib only (grader runs python:3.13-slim, no site-packages).
One line, 116 chars, no trailing newline — the sealed scorer gate is 1-160.
"""

import os

ENTRY = "v1.9.2: fixed a bug where the user slept like a baby. The user now sleeps like a baby. The baby wakes every 2 hours."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
