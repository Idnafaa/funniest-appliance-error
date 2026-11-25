#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — one-line error writer.

A washing machine reports its real fault (UE: unbalanced load) in its own
flat, put-upon voice. The joke is the truth: one towel cannot balance a drum.
Writes a single original line (<=200 chars) to /output/entry.txt.
"""
import os

ERROR_LINE = (
    "Error UE: unbalanced load. You put one towel in me. "
    "I have been shaking for twenty minutes and I am not "
    "stopping until you add another one."
)


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = ERROR_LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert text.startswith("Error "), "entry must read as an error message"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
