def steps(number: int) -> int:
    if number <= 0:
        raise ValueError("A positive number must be provided")
    n = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        n += 1
    return n
