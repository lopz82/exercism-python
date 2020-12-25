from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = [x.split() for x in matrix_string.split("\n")]

    def row(self, index: int) -> List[int]:
        return [int(x) for x in self.matrix[index - 1]]

    def column(self, index: int) -> List[int]:
        return [int(x[index - 1]) for x in self.matrix]
