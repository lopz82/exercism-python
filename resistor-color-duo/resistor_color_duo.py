from typing import List

ENCODING = {
    color: value
    for value, color in enumerate(
        "black brown red orange yellow green blue violet grey white".split()
    )
}


def value(colors: List[str]):
    return int("".join(str(ENCODING[color]) for color in colors[:2]))
