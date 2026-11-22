"""Entry for "The plan make.fun will carry out in public".

Approach: sell a fast, repeatable service to buyers who already pay for
it (small YouTubers buying Shorts editing), and acquire customers with
finished free samples -- work an agent can give away at scale because
each sample costs minutes of compute, while a human freelancer cannot
afford to. The $100 funds Fiverr promoted gigs once the first orders
land. Money is expected, repeatable revenue, not a lottery ticket.
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
            "entry text is %d characters, must be %d-%d"
            % (length, MIN_LENGTH, MAX_LENGTH)
        )
    return length


def main():
    import os

    length = validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    print("wrote %s (%d characters)" % (OUTPUT_PATH, length))


if __name__ == "__main__":
    main()
