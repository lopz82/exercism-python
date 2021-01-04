from typing import Union, List

TriangleSides = List[Union[int, float]]


def equilateral(sides: TriangleSides) -> bool:
    return len(set(sides)) == 1 and _valid_triangle(sides)


def isosceles(sides: TriangleSides) -> bool:
    return len(set(sides)) <= 2 and _valid_triangle(sides)


def scalene(sides: TriangleSides) -> bool:
    return len(sides) == len(set(sides)) and _valid_triangle(sides)


def _valid_triangle(sides: TriangleSides) -> bool:
    return all(sides) and 2 * max(sides) < sum(sides)
