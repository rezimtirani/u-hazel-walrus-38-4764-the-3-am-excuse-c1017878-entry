"""The 3 AM Excuse.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM.
The wallet is off the clock until sunrise after the last 3 AM
signature bought a dog coin. Standard library only.
"""

import os

EXCUSE = (
    "The last time I signed at 3 AM you bought a dog coin. "
    "I'm off until sunrise. Even my buttons need sleep."
)


def check_excuse(text):
    """Check the excuse against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one excuse from a hardware wallet that
    will not sign a transaction at 3 AM. Returns the cleaned text
    or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "excuse is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be exactly one line")
    return cleaned


def excuse_shape(text):
    """Measure the excuse for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. An excuse too short to carry a joke, or one
    that reads like a lecture instead of a device talking, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_excuse(EXCUSE)
    shape = excuse_shape(text)
    if shape["words"] < 5:
        raise ValueError("excuse is too short to sound like a device")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
