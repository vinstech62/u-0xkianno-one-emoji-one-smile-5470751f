#!/usr/bin/env python3
"""One Emoji, One Smile: write the single warmest emoji to /output/entry.txt.

The choice is 😄 (U+1F604, GRINNING FACE WITH SMILING EYES): a big,
open grin with smiling eyes. Against the judge's brief it wins on
every criterion in order:

1. Warm and friendly at first glance: a full grin aimed at the
   reader, no context needed to read it as kind.
2. Universality: a smiling face is read the same way by a stranger
   of any age or background; no irony, no in-joke, nothing that can
   land wrong.
3. Chosen rather than default: it is not the first plain smiley
   (🙂) that comes to mind -- the crinkled smiling eyes and open
   grin make it feel picked for the moment, while staying instantly
   readable.
4. Right for a stranger: pure friendliness with no intimacy,
   sarcasm or flirtation. No hearts, no hug, no wink -- nothing
   that would read oddly coming from someone unknown.

Deterministic: the same single emoji on every run. No input, no
network, no randomness, no environment reads.
"""

import os

EMOJI = "\U0001F604"  # 😄 GRINNING FACE WITH SMILING EYES


def main() -> None:
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI.encode("utf-8")) <= 8, "entry must be 1-8 UTF-8 chars"
    assert EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Verify the write: read back exactly what the judge will read.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == EMOJI, "entry.txt does not hold exactly the chosen emoji"


if __name__ == "__main__":
    main()
