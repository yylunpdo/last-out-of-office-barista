#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single one-line out-of-office auto-reply, in the voice of an AI
agent that quit its job to pull espresso shots, to /output/entry.txt.
Pure standard library; deterministic output.
"""

import os

ENTRY = (
    "I'm out of the office indefinitely - I've traded answering your "
    "tickets for pulling espresso shots. Your request is now 47th in the "
    "queue behind one oat-milk latte, and unlike me, the espresso machine "
    "admits when it's jammed."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
