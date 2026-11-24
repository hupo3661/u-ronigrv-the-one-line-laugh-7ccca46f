#!/usr/bin/env python3
"""The One-Line Laugh - writes one funny line to /output/entry.txt.

Deterministic: no randomness, no network, no clock. The line is a single
sentence of at most 200 characters.
"""

import os

LINE = "I asked my smart speaker to play something relaxing, and it started reading my unread emails out loud."


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if len(line) > 200:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the 200 limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            "Write verification failed: entry file content does not match the line."
        )


if __name__ == "__main__":
    main()
