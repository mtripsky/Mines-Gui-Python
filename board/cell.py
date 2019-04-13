class Cell():
    """Structure of Cell on board"""

    def __init__(self):
        self.isRevealed = False
        self.isMine = False
        self.neighborMinesCount = 0
        self.clickCounter = 0
