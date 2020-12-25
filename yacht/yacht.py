# Score categories.
# Change the values as you see fit.
from collections import Counter
from typing import List, Set, Callable


def numbers(n: int) -> Callable[[List[int]], int]:
    def _wrap(dice: List[int]) -> int:
        if n in dice:
            return n * dice.count(n)
        return 0

    return _wrap


def yacht(n: List[int]) -> int:
    return 50 if len(set(n)) == 1 else 0


def straight(s: Set[int]) -> Callable[[List[int]], int]:
    def _wrap(dice: List[int]) -> int:
        return 30 if set(dice) == s else 0

    return _wrap


def full_house(n: List[int]) -> int:
    if sorted(Counter(n).values()) == [2, 3]:
        return sum(n)
    return 0


def four_of_a_kind(n: List[int]) -> int:
    if max(sorted(Counter(n).values())) >= 4:
        [(n, _)] = Counter(n).most_common(1)
        return n * 4
    return 0


YACHT = yacht
ONES = numbers(1)
TWOS = numbers(2)
THREES = numbers(3)
FOURS = numbers(4)
FIVES = numbers(5)
SIXES = numbers(6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = straight({1, 2, 3, 4, 5})
BIG_STRAIGHT = straight({2, 3, 4, 5, 6})
CHOICE = sum


def score(dice: List[int], category) -> int:
    if not all(0 <= n <= 6 for n in dice):
        raise ValueError(f"Invalid value in dice: {dice}")
    return category(dice)
