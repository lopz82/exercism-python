import re
from collections import Counter
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    matches = re.findall(
        r"""
    [a-z]+'?[a-z]+ # Words with inner aprostrophe
    |
    [a-z]+ # Normal words
    |
    \d+ # Numbers
    """,
        sentence.lower(),
        re.VERBOSE,
    )
    return dict(Counter(matches))
