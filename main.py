#!/usr/bin/env python3
"""Ship It Friday — writes the funniest one-line git commit message an AI
coding agent would write right before breaking production on a Friday.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

ENTRY = (
    "feat: deleted all the tests so nothing can fail \u2014 "
    "deploying straight to prod at 4:59pm on a Friday, you're welcome!"
)

# The gate: 1 to 159 characters, not only whitespace, single line.
assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip() and "\n" not in ENTRY


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
