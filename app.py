from board.state import State
from board.minesGenerator import MinesGenerator
from board.boardInitializer import BoardInitializer
from board.boardUpdater import BoardUpdater
from game.boardWidget import BoardWidget
from tkinter import *

state = State(10, 10)
updater = BoardUpdater(state)
generator = MinesGenerator()
initializer = BoardInitializer(state, generator, updater)
initializer.initiate()

root = Tk()
frame = Frame(root, width=600, height=600)
frame.pack()
b = BoardWidget(state, frame)
root.mainloop()
