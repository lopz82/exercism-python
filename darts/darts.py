import math


def score(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    if r > 10:
        return 0
    elif 10 >= r > 5:
        return 1
    elif 5 >= r > 1:
        return 5
    return 10
