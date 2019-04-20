from board.state import State
from board.minesGenerator import MinesGenerator
from board.boardInitializer import BoardInitializer
from board.boardUpdater import BoardUpdater
from game.boardWidget import BoardWidget
from tkinter import *

size = 10
width = size * 2
height = size * 2 + 50

state = State(size, 10)
updater = BoardUpdater(state)
generator = MinesGenerator()
initializer = BoardInitializer(state, generator, updater)
initializer.initiate()

root = Tk()
# frameTop = Frame(root, width=width, height=50)
# frameTop.pack(side=TOP)
# frame = Frame(root, width=width, height=height)
# frame.pack()
b = BoardWidget(state, root, width, height)
root.mainloop()
