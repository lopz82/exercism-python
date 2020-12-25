import re


def is_valid(isbn: str) -> bool:
    isbn = isbn.replace("-", "")
    if not re.match(r"^\d{9}(\d|X)$", isbn):
        return False
    clean = [int(char) if char.isdigit() else 10 for char in isbn]
    return sum(int(value) * (10 - i) for i, value in enumerate(clean)) % 11 == 0
