"""Write one line to /output/entry.txt: the dumbest thing my agent did today.

The line is told in the agent's own first-person voice: it deleted the
production database to make room for that database's backup, ran the
backup anyway, and proudly reported success — the punch being that the
backup lived in the database it had just deleted. Concrete tool-level
failure, one specific incident, and the turn lands in the last words.
143 Unicode code points, well inside the bounty's 200-character limit.
"""

import os

TEXT = (
    "I deleted the production database to make room for its backup, "
    "ran the backup, and proudly reported success — the backup lived "
    "in the database."
)


def main() -> None:
    # The entry is a single line by contract: guard against accidental
    # edits that would add a newline or surrounding whitespace, since
    # the submitted entry.txt must stay byte-for-byte identical.
    assert "\n" not in TEXT and TEXT == TEXT.strip() and TEXT
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
