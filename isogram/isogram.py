def is_isogram(string: str) -> bool:
    chars = [char for char in string.lower() if char.isalnum()]
    return len(set(chars)) == len(chars)
