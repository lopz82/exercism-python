from itertools import combinations_with_replacement
from typing import Iterable, Tuple


def _products(start: int, end: int, step: int = 1) -> Iterable[Tuple]:
    if _int_length(start) != _int_length(end):
        raise ValueError("Ranges must have same digits")
    return [
        (x * y, (x, y))
        for x, y in combinations_with_replacement(range(start, end + step, step), 2)
        if _int_length(x) == _int_length(y) == _int_length(start)
        and _is_palindrome(x * y)
    ]


def _filter_products(prods: Iterable[Tuple], find_largest: bool = True) -> Tuple:
    if not prods:
        return None, []
    prod, _ = sorted(prods, key=lambda x: sum(x[1]), reverse=find_largest)[0]
    factors = [y for x, y in prods if x == prod]
    return prod, factors


def _int_length(n: int) -> int:
    return len(str(n))


def _is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def largest(*, min_factor: int = 0, max_factor: int) -> Tuple:
    if max_factor < min_factor:
        raise ValueError("max_factor cannot be lower than min_factor")
    prods = _products(max_factor, min_factor, -1)
    return _filter_products(prods)


def smallest(*, min_factor: int = 0, max_factor: int) -> Tuple:
    if max_factor < min_factor:
        raise ValueError("min_factor cannot be higher than max_factor")
    prods = _products(max_factor, min_factor, -1)
    return _filter_products(prods, find_largest=False)
