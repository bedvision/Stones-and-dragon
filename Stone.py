import random

from config import *


class Stone:

    def __init__(self, i):
        self.id = i
        self.x = random.randint(0, WIDTH / 60)
        self.y = random.randint(0, HEIGHT / 60)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
