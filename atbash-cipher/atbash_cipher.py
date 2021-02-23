from string import ascii_lowercase

ENCODE = {
    **dict(zip(ascii_lowercase, ascii_lowercase[::-1])),
    **dict(zip(list("1234567890"), list("1234567890"))),
}

DECODE = {
    **dict(zip(ascii_lowercase[::-1], ascii_lowercase)),
    **dict(zip(list("1234567890"), list("1234567890"))),
}


def encode(plain_text: str) -> str:
    plain_text = "".join(ENCODE[char.lower()] for char in plain_text if char.isalnum())
    return " ".join(plain_text[n : n + 5] for n in range(0, len(plain_text), 5))


def decode(ciphered_text: str) -> str:
    return ciphered_text.replace(" ", "").translate(str.maketrans(DECODE))
