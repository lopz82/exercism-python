SCORES = {
    letter: score
    for letters, score in (
        ("A E I O U L N R S T".split(), 1),
        ("D G".split(), 2),
        ("B C M P".split(), 3),
        ("F H V W Y".split(), 4),
        (["K"], 5),
        ("J X".split(), 8),
        ("Q Z".split(), 10),
    )
    for letter in letters
}


def score(word: str) -> int:
    return sum(SCORES[char] for char in word.upper())
