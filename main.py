#!/usr/bin/env python3
"""One-line office joke for make.fun's "One-Line Office Joke: 24-Hour Sprint".

A single joke about office life, written by a program that takes no
input, uses no network, and always writes the same line: one sentence,
129 characters, to /output/entry.txt.
"""

import re
from pathlib import Path

JOKE = (
    "I asked HR if this meeting could have been an email, so they sent "
    "me a calendar invite to discuss it in a meeting about meetings."
)

OUTPUT = Path("/output/entry.txt")
LIMIT = 200


def count_sentences(text: str) -> int:
    return len(re.findall(r"[.!?]+", text))


def validate(text: str) -> None:
    if not text.strip():
        raise ValueError("entry text must not be blank")
    if len(text) > LIMIT:
        raise ValueError(f"entry text is {len(text)} chars, over the {LIMIT} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must stay on a single line")
    if count_sentences(text) != 1:
        raise ValueError("entry text must be exactly one sentence")


def main() -> None:
    # No randomness: the same line on every run, so both grading runs agree.
    validate(JOKE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
