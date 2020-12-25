from typing import Generator


def classify(number: int) -> str:
    if number <= 0:
        raise ValueError("number must be greater than 0")
    aliquot_sum = sum(aliquot(number))
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"


def aliquot(n: int) -> Generator[int]:
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
