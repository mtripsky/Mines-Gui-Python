import random
from helpers.coordinate import Coordinate


class MinesGenerator():
    """Generates random mines coordinates"""

    def generate(self, size, count):
        result = list(
            [Coordinate(x, y) for x in range(size) for y in range(size)])
        random.shuffle(result)

        return result[0:count]
