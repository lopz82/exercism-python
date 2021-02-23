from typing import List

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(one: List[int], two: List[int]) -> int:
    if one == two:
        return EQUAL
    elif len(one) > len(two) and _is_contained(one, two):
        return SUPERLIST
    elif len(two) > len(one) and _is_contained(two, one):
        return SUBLIST
    else:
        return UNEQUAL


def _is_contained(container: List[int], contained: List[int]) -> bool:
    return any(
        contained == pair
        for pair in (container[n : n + len(contained)] for n in range(len(container)))
    )
