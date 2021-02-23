from typing import List, Optional


class Garden:
    CHILDREN = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()
    PLANTS = {
        plant[0].upper(): plant for plant in "Grass Clover Radishes Violets".split()
    }

    def __init__(self, diagram: str, students: Optional[List[str]] = None):
        self.garden = [list(row) for row in diagram.split("\n")]
        self.students = sorted(students) if students else Garden.CHILDREN

    def plants(self, student) -> List[str]:
        i = self.students.index(student)
        plants = []
        for row in self.garden:
            plants.extend(row[i * 2 : (i + 1) * 2])
        return [Garden.PLANTS[plant] for plant in plants]
