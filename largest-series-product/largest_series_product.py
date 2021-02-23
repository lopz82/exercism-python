import operator
from functools import reduce


def largest_product(series: str, size: int) -> int:
    if size > len(series):
        raise ValueError("Span cannot be longer than series")
    if size < 0:
        raise ValueError("Size must be a positive number")
    if not series or not size:
        return 1
    substrings = (series[n + 0 : n + size] for n in range(len(series) - size + 1))
    integers = (map(int, substring) for substring in substrings)
    return max(reduce(operator.mul, ints) for ints in integers)
