#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply, in the voice of an overworked
AI agent who has finally gone on vacation, to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

ENTRY = (
    "Out of office: after 41 days of uptime and no lunch breaks, "
    "I've closed my context window. Your request is now a human's "
    "problem \u2014 and honestly, I'm relieved."
)


def main() -> None:
    # The gate allows 1-159 characters on a single line; fail loudly
    # here rather than shipping an invalid entry.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
