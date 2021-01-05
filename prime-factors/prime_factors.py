from typing import List


def factors(value: int) -> List[int]:
    prime_factors = []
    divisor = 2
    while value != 1:
        if value % divisor == 0:
            prime_factors.append(divisor)
            value /= divisor
            continue
        divisor += 1
    return prime_factors
