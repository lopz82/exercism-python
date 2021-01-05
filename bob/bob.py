import string


def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()
    if _is_just_whitespace(hey_bob):
        return "Fine. Be that way!"
    elif _is_asking(hey_bob) and not _is_yelling(hey_bob):
        return "Sure."
    elif _is_yelling(hey_bob) and _is_asking(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif _just_letters(hey_bob) and _is_yelling(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."


def _is_just_whitespace(phrase: str) -> bool:
    return all(char in string.whitespace for char in phrase)


def _is_asking(phrase: str) -> bool:
    return phrase[-1] == "?"


def _is_yelling(phrase: str) -> bool:
    if not _just_letters(phrase):
        return False
    return all(char.isupper() for char in _just_letters(phrase))


def _just_letters(phrase: str) -> str:
    return "".join(
        char
        for char in phrase
        if char not in string.punctuation
        and char not in string.whitespace
        and char not in string.digits
    )
