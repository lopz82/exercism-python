RAINDROPS = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}


def convert(number: int) -> str:
    result = "".join(value for key, value in RAINDROPS.items() if number % key == 0)
    return result or str(number)
