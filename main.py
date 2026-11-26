#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
"""

import os

JOKE = "I asked HR if my chair could file a complaint about me — it said I sit on it all day and never once asked how it feels."

def main():
    # Gate: entry must be 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
