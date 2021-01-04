from collections import Counter
from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    return [
        candidate
        for candidate in candidates
        if Counter(candidate.lower()) == Counter(word.lower())
        and candidate.lower() != word.lower()
    ]
