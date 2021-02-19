import re


def decode(string: str) -> str:
    return re.sub(r"(\d*)(\D)", lambda x: x.group(2) * int(x.group(1) or 1), string)


def encode(string: str) -> str:
    return re.sub(
        r"(.)\1*",
        lambda x: f"{len(x.group(0)) if len(x.group(0)) > 1 else ''}{x.group(1)}",
        string,
    )
