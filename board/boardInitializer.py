class BoardInitializer():
    """
    It initialize board based on coordinates of generated mines,
    then it updates all neighbors of the mine
    """

    def __init__(self, state, generator, updater):
        super().__init__()
        self._state = state
        self._generator = generator
        self._updater = updater

    def initiate(self):
        for coordinate in self._generator.generate(
                self._state.getBoardSize(), self._state.getMinesCount()):
            self._updater.update(coordinate)
