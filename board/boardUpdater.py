from helpers.boardReferee import BoardReferee
from helpers.coordinate import Coordinate


class BoardUpdater():
    """Updates all neighbors of mine"""

    def __init__(self, state):
        super().__init__()
        self._state = state

    def update(self, coord):
        if (BoardReferee.isCoordinateOnBoard(coord,
                                             self._state.getBoardSize())):
            self._state.getCell(coord).isMine = True
            self._state.getCell(coord).symbol = 'm'
            neighbors = self.__getCellNeighbors(coord)

            for neighbor in neighbors:
                if (BoardReferee.isCoordinateOnBoard(
                        neighbor, self._state.getBoardSize())):
                    self._state.getCell(neighbor).neighborMinesCount += 1
                    self._state.getCell(neighbor).symbol = self._state.getCell(
                        neighbor).neighborMinesCount

    def __getCellNeighbors(self, coord):
        return list([
            Coordinate(coord.X + i, coord.Y + j) for i in range(-1, 2)
            for j in range(-1, 2) if not (i == 0 and j == 0)
        ])
