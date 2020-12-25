def is_armstrong_number(number: int) -> bool:
    length = len(str(number))
    return number == sum(int(num) ** length for num in str(number))
