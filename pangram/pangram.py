ALPHABET = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def is_pangram(sentence):
    filtered = set(letter.upper() for letter in sentence if letter.isalpha())
    return filtered == ALPHABET
