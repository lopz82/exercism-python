from itertools import count


def prime(number: int) -> int:
    if number <= 0:
        raise ValueError("Index must be positive")
    primes = 0
    marked = set()
    while primes <= number:
        for num in count(start=2):
            if num not in marked:
                marked.update(x for x in range(num, number * 20, num))
                primes += 1
                if primes == number:
                    return num
