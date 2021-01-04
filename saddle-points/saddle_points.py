from typing import Dict, List


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Irregular matrix")
    points = []
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if all(item >= x for x in row) and all(item <= x[j] for x in matrix):
                points.append({"row": i + 1, "column": j + 1})
    return points
