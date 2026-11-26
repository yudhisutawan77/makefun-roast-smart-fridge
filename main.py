"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes one roast line (at most 160 characters) to the entry output
file. Python 3.13, standard library only, no network, fully
deterministic: every run produces byte-identical output.
"""

import os
import sys

# Bootstrap: put this file's directory at the front of sys.path so the
# module resolves the same way no matter which working directory the
# grader invokes it from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MAX_CHARS = 160


def resolve_output_path():
    """Decide where the entry text is written.

    Priority, in order:
      1. ENTRY_OUT, when set: a file path, unless it names an existing
         directory, in which case entry.txt inside that directory.
      2. MAKEFUN_OUTPUT_DIR, when set: entry.txt inside that directory.
      3. /output/entry.txt (the grader's writable output directory).
      4. entry.txt in the current working directory (last resort).
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        return os.path.join(output_dir, "entry.txt")

    return os.path.join("/output", "entry.txt")


def write_entry_text(path, text):
    """Write *text* to *path* as UTF-8, creating parent dirs as needed."""
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


# The roast: one line, one sentence. The fridge's ice dispenser held
# hostage by a firmware update is a real smart-fridge behaviour, and
# the sting lands on the Terms of Service nobody ever reads.
ENTRY_TEXT = (
    "My smart fridge won't give me ice until it finishes updating, "
    "so my drink is held hostage by a Terms of Service I never read."
)


def check_entry_text(text):
    """Enforce the gate: 1 to 160 UTF-8 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("entry text is %d chars, over %d" % (len(text), MAX_CHARS))
    return text


def main():
    text = check_entry_text(ENTRY_TEXT)
    write_entry_text(resolve_output_path(), text)


if __name__ == "__main__":
    main()
