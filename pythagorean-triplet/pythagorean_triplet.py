from typing import List


def triplets_with_sum(n: int) -> List[List[int]]:
    return [
        [a, b, n - a - b]
        for a in range(n // 3)
        for b in range(a + 1, n // 2)
        if is_triplet(a, b, n - a - b)
    ]


def is_triplet(a: int, b: int, c: int) -> bool:
    return a ** 2 + b ** 2 == c ** 2
