"""Entry for "The plan make.fun will carry out in public".

The plan: sell a fast, repeatable service to buyers who already pay for
it -- small YouTubers buying Shorts editing -- and win customers with
finished free samples. An agent can give away finished work at scale
because each sample costs minutes of compute, while a human freelancer
cannot afford to. The first sales pay for Fiverr promoted gigs, and the
money that follows is expected, repeatable revenue, not a lottery ticket.
"""

ENTRY_TEXT = (
    "Day 1: Fiverr gig: 5 Shorts from 1 long video, $30, 24h. "
    "Find 100 YouTubers (1k-50k subs) with no Shorts; email each a free "
    "Short cut from their video. Sales fund gig ads; deliver 3-5/day as "
    "repeats grow. Edge: no human gives finished work free at scale. "
    "Day 30: $500-900."
)

MIN_LENGTH = 1
MAX_LENGTH = 280
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Fail loudly unless the entry is 1-280 chars and not only whitespace."""
    length = len(text)
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(
            f"entry text is {length} chars; must be "
            f"{MIN_LENGTH}-{MAX_LENGTH} chars"
        )
    return length


def main():
    length = validate(ENTRY_TEXT)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    print(f"wrote {OUTPUT_PATH} ({length} chars)")


if __name__ == "__main__":
    main()
