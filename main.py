#!/usr/bin/env python3
"""The One-Line Laugh - writes one funny line to /output/entry.txt.

Deterministic: no randomness, no network, no clock. The line is a single
sentence of at most 200 characters.
"""

import os

LINE = "I asked my smart speaker to play something relaxing, and it started reading my unread emails out loud."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
