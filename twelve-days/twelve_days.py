from typing import List

GIFTS = """twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing,
 eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, 
four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree""".replace(
    "\n", ""
).split(
    ", "
)

DAYS = "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth".split()


def recite(start_verse: int, end_verse: int) -> List[str]:
    return [verse(n) for n in range(start_verse - 1, end_verse)]


def verse(num: int) -> str:
    return f"On the {DAYS[num]} day of Christmas my true love gave to me: {GIFTS[-1].replace('and ', '') if num == 0 else ', '.join(GIFTS[-num - 1:])}."
