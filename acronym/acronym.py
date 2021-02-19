import re


def abbreviate(words: str) -> str:
    return "".join(
        word[0].upper() for word in re.findall(r"[A-Za-z]+'?[A-Za-z]*", words)
    )
