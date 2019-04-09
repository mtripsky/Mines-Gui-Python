import numpy as np
from board.field import Field

class State():
    """docstring for ."""
    def __init__(self, size):
        self.size = size
        self.fields = np.array([[Field() for _ in range(size)] for _ in range(size)])


    def print(self):
        for i  in range(self.size):
            for j in range(self.size):
                print(f'{self.fields[i]} ')
