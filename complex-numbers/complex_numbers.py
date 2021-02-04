import math
import numbers


class ComplexNumber:
    def __init__(self, real: int, imaginary: int):
        self.r = real
        self.i = imaginary

    def __eq__(self, other: "ComplexNumber") -> bool:
        return self.r == other.r and self.i == other.i

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        if isinstance(other, numbers.Real):
            return ComplexNumber(self.r * other, self.i)
        return ComplexNumber(
            self.r * other.r - self.i * other.i,
            self.i * other.r + self.r * other.i,
        )

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.r - other.r, self.i - other.i)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            (self.r * other.r + self.i * other.i) / (other.r ** 2 + other.i ** 2),
            (self.i * other.r - self.r * other.i) / (other.r ** 2 + other.i ** 2),
        )

    def __abs__(self) -> float:
        return math.sqrt(self.r ** 2 + self.i ** 2)

    def conjugate(self) -> "ComplexNumber":
        return ComplexNumber(self.r, -self.i)

    def exp(self) -> "ComplexNumber":
        return ComplexNumber(math.cos(self.i), math.sin(self.i)) * math.exp(self.r)
