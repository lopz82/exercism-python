from typing import List


def slices(series: str, length: int) -> List[str]:
    if not series:
        raise ValueError("Empty series")
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    if length > len(series):
        raise ValueError("Length cannot be larger than the series")
    return [
        series[i : i + length] for i in range(len(series)) if i + length <= len(series)
    ]
