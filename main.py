#!/usr/bin/env python3
"""Entry for make.fun's "One-Line Office Joke: 24-Hour Sprint" bounty.

Writes one funny line about office life (one sentence, at most
200 characters) to /output/entry.txt. No network, no input,
deterministic.
"""

import os
import re


def sentence_count(text: str) -> int:
    return len(re.findall(r"[.!?]+", text))


TEXT = (
    "I asked HR if this meeting could have been an email, so they sent "
    "me a calendar invite to discuss it in a meeting about meetings."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    if sentence_count(TEXT) != 1:
        raise ValueError(
            f"entry text must be exactly 1 sentence, got {sentence_count(TEXT)}"
        )
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line, no line breaks")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
