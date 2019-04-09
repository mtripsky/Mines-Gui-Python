import numpy as np
import random
from helpers.coordinate import Coordinate

class MinesGenerator():
    """docstring for MinesGenerator."""

    def generate(self, size, count):
        result = list([Coordinate(x, y) for x in range(size) for y in range(size)])
        random.shuffle(result)

        return result[0:count]
