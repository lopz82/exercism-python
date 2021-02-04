import random


class Cipher:
    ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

    def __init__(self, key=None):
        random.seed(42)
        self.key = key or "".join(
            Cipher.ALPHABET[random.randint(0, len(Cipher.ALPHABET) - 1)]
            for _ in range(10)
        )
        self.shifts = [self.to_value(c) for c in self.key]

    def encode(self, text):
        return "".join(
            self.to_char(self.to_value(x) + self.shifts[i % len(self.shifts)])
            for i, x in enumerate(text)
        )

    def decode(self, text):
        return "".join(
            self.to_char(self.to_value(x) - self.shifts[i % len(self.shifts)])
            for i, x in enumerate(text)
        )

    def to_value(self, char):
        return Cipher.ALPHABET.index(char)

    def to_char(self, value):
        return Cipher.ALPHABET[value % len(Cipher.ALPHABET)]
