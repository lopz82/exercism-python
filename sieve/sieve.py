from typing import List


def primes(limit: int) -> List[int]:
    marked = set()
    result = []
    for num in range(2, limit + 1):
        if num not in marked:
            marked.update(num * x for x in range(num, round((limit + 1) / 2)))
            result.append(num)
    return result
