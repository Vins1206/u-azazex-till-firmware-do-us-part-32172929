#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence, under 200 characters, to /output/entry.txt:
a machine's own wedding vow, funny and heartfelt at the same time.
Pure standard library, deterministic: every run writes the same bytes.

Why this line: it is spoken first-person by the robot at its own wedding,
the joke grows out of the situation (a robot treating a marriage like
software it refuses to wipe), the tenderness sits underneath it, and every
machine word — factory-reset, bugs, feature, patch — is the robot's own.
"""

import os

VOW = (
    "I promise never to factory-reset us, no matter how many bugs we find, "
    "because you are the only feature I would never patch out."
)


def main() -> None:
    text = VOW.strip()
    assert 1 <= len(text) <= 200, f"vow is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "vow must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
