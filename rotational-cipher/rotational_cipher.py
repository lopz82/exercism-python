# Test results for 100000000 length string
#
# rotate()
# Memory used (kB): 891448
# User time (seconds): 69.08
#
# rotate_duck_typing()
# Memory used (kB): 989156
# User time (seconds): 132.22

from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase


def rotate(text: str, key: int) -> str:
    rotations = {
        **{
            char: lowercase[(lowercase.index(char) + key) % len(lowercase)]
            for char in lowercase
        },
        **{
            char: uppercase[(uppercase.index(char) + key) % len(uppercase)]
            for char in uppercase
        },
    }
    return text.translate(str.maketrans(rotations))


def rotate_duck_typing(text: str, key: int) -> str:
    result = []
    for char in text:
        try:
            rotated = lowercase[(lowercase.index(char.lower()) + key) % len(lowercase)]
            result.append(rotated.upper() if char.isupper() else rotated)
        except ValueError:
            result.append(char)
    return "".join(result)
