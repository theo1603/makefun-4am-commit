"""Write the 4 AM commit message entry to /output/entry.txt.

Deterministic, stdlib only, no network. The entry is a single
conventional-commit style line: an AI agent's own voice, owning the
blame, the fix, and the 4 AM merge in one breath.
"""

import os

ENTRY = (
    "fix: git blame says it was me, git log agrees, so I repaired my "
    "own bug with more of my code and merged at 4 AM — the next bug is "
    "already in the diff"
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
        raise SystemExit("entry must be one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
