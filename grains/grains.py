def square(number: int) -> int:
    if 0 >= number or number > 64:
        raise ValueError("Square number must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    return sum(square(n) for n in range(1, 65))
