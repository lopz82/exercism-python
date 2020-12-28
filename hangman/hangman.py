# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word: str):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guesses = set()

    def _right_but_repeated(self, char):
        return char in self.word and char in self.guesses

    def guess(self, char: str) -> None:
        if self.status != STATUS_ONGOING:
            raise ValueError("The game is over")
        if char not in self.word or self._right_but_repeated(char):
            self.remaining_guesses -= 1
        self.guesses.add(char.lower())
        self.status = self.get_status()

    def get_masked_word(self) -> str:
        return "".join("_" if char not in self.guesses else char for char in self.word)

    def get_status(self) -> str:
        if set(self.word) <= set(self.guesses):
            return STATUS_WIN
        if self.remaining_guesses < 0:
            return STATUS_LOSE
        return STATUS_ONGOING
