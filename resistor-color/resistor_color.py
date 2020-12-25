from typing import List


ENCODING = {
    color: value
    for value, color in enumerate(
        "black brown red orange yellow green blue violet grey white".split()
    )
}


def color_code(color: str) -> int:
    return ENCODING[color]


def colors() -> List[str]:
    return list(ENCODING.keys())
