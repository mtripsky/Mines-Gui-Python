class BoardReferee(object):
    """Board referee if given coordinate is on the board"""

    def __init__(self):
        super().__init__()

    @staticmethod
    def isOnBoard(x, y, size):
        if (x < 0 or y < 0 or x >= size or y >= size):
            return False

        return True

    @staticmethod
    def isCoordinateOnBoard(coord, size):
        if (coord.X < 0 or coord.Y < 0 or coord.X >= size or coord.Y >= size):
            return False

        return True
