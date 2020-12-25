import math
import random
from datetime import datetime


def modifier(n):
    return math.floor((n - 10) / 2)


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        random.seed(datetime.now())
        dices = [random.randint(1, 7) for _ in range(4)]
        return sum(sorted(dices, reverse=True)[:3])
