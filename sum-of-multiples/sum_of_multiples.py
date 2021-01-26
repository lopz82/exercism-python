from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    found = []
    for multiple in multiples:
        found.extend(n for n in range(limit-1, 0, -1) if multiple != 0 and n % multiple == 0)
    return sum(set(found))
