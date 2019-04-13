import numpy as np
from board.cell import Cell
from helpers.coordinate import Coordinate


class State():
    """State of the board"""

    def __init__(self, size, minesCount):
        self._size = size
        self._cells = np.array([[Cell() for _ in range(size)]
                                for _ in range(size)])
        self._minesCount = minesCount

    def getCell(self, coordinate):
        return self._cells[coordinate.X, coordinate.Y]

    def getBoardSize(self):
        return self._size

    def getMinesCount(self):
        return self._minesCount

    def print(self):
        dim = self._cells.shape
        for x in range(dim[0]):
            line = ""
            for y in range(dim[1]):
                line += f'{self._cells[x,y].symbol} '
            print(line)
