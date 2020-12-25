import datetime
import random
import string


class Robot:
    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        random.seed(datetime.datetime.now())
        letters = string.ascii_uppercase
        chars = [random.choice(letters) for i in range(2)]
        nums = [str(random.randint(0, 9)) for i in range(3)]
        self.name = "".join(chars + nums)
