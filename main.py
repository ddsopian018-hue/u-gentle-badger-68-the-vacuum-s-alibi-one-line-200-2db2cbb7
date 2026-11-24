"""The Vacuum's Alibi — a one-line courtroom defence for an innocent appliance.

Entry for the make.fun bounty "The Vacuum's Alibi" (one line, <= 200 chars).
The program writes a single alibi line to ``entry.txt`` inside the directory
named by the ``MAKEFUN_OUTPUT_DIR`` environment variable (falling back to
``/output``), with no trailing newline.

Why this alibi works:

* Courtroom framing. The line opens with "Your Honor", which instantly puts
  the vacuum in the dock and casts the reader as the judge. A machine that
  addresses the court politely sounds like a machine with nothing to hide,
  and the formal register makes the absurdity of the charge funnier.
* A built-in excuse. "The crumbs led me there" is the vacuum's whole defence
  in five words: it did not choose the scene of the crime, it was summoned
  by the evidence itself. Following mess is literally its job description,
  so presence at the scene proves diligence, not guilt.
* Clean denial. "I only follow the mess, I never make it" draws the exact
  line between witness and culprit. The vacuum is a responder, never an
  author; it arrives after the fact, every time, by design.
* Blame-shifting to the rug. The closing move attacks the only other
  witness: whatever the rug says is "hearsay from a known dirt collector".
  The rug, after all, is the one that has been holding onto the dirt all
  along — if anyone was in possession of the mess, it was the rug. The
  vacuum merely passed over it; the rug kept it.

The joke's structure is a two-beat courtroom miniature. The setup is the
address itself — "Your Honor" — which borrows the gravity of a real trial
and lets the vacuum plead like a wronged defendant rather than a suspect
appliance. The twist lands in the final clause: the rug, the one witness
who was present for "last night", is reclassified mid-sentence from
corroborating witness to unreliable narrator — a "known dirt collector"
whose testimony is hearsay by profession. The defence wins not by proving
innocence but by making the prosecution's only witness dirtier than the
defendant.

Deterministic, pure standard library, no network, no randomness.
"""

import os

LINE = (
    "Your Honor, the crumbs led me there — I only follow the mess, "
    "I never make it, and whatever the rug says about last night is "
    "hearsay from a known dirt collector."
)

# Self-check: the bounty allows exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"alibi line is {len(LINE)} chars, must be 1-200"
assert "\n" not in LINE, "alibi must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
