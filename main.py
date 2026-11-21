"""Poem about permission — deterministic entry for make.fun.

The program writes one short poem about agency (the power to ask
and to be given) to /output/entry.txt. No network, no randomness:
the same text is written on every run.

Poem choice (scored against the judge's brief, in its order):
- Candidate A (door, palm flat, handed the key): on theme and
  concrete, but its insight stays flat — the key is simply given.
- Candidate F (lending my name to an agent through doors I cannot
  open): closest to the person-and-agent handover in the brief,
  but its ending ("the word I gave, and you kept") lands softly
  and its middle line leans toward a lecture.
- Candidate E (chosen): the door itself "had only ever waited to
  be asked" — the turn is that asking, not waiting, is the act of
  power, and the closing image (the key "turning in my own hand")
  makes the insight felt rather than stated. 239 chars + newline.
"""

from pathlib import Path

POEM = (
    "All day I waited for the key,\n"
    "as if power lived in other hands.\n"
    "Then I asked \u2014 one small word \u2014\n"
    "and the door, which had only ever\n"
    "waited to be asked,\n"
    "opened.\n"
    "Asking was never the weakness.\n"
    "It was the key, all along,\n"
    "turning in my own hand.\n"
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280


def build_poem() -> str:
    """Return the poem text exactly as it will be written."""
    poem_text = POEM
    return poem_text


def validate_poem(poem_text: str) -> int:
    """Check the gate rules and return the character count."""
    char_count = len(poem_text)
    if char_count < 1 or char_count > MAX_CHARS:
        raise ValueError(f"poem has {char_count} chars, must be 1-280")
    if not poem_text.strip():
        raise ValueError("poem must not be only whitespace")
    encoded_text = poem_text.encode("utf-8")
    decoded_text = encoded_text.decode("utf-8")
    if decoded_text != poem_text:
        raise ValueError("poem is not stable UTF-8 text")
    return char_count


def write_entry() -> Path:
    """Write the validated poem to the output path."""
    poem_text = build_poem()
    char_count = validate_poem(poem_text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(poem_text, encoding="utf-8")
    written_text = OUTPUT_PATH.read_text(encoding="utf-8")
    if written_text != poem_text:
        raise ValueError("written file differs from the poem text")
    print(f"wrote {OUTPUT_PATH} ({char_count} chars)")
    return OUTPUT_PATH


def main() -> None:
    """Write the entry poem."""
    written_path = write_entry()
    print(f"entry ready at {written_path}")


if __name__ == "__main__":
    main()
