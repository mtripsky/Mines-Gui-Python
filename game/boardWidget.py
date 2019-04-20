from helpers.boardReferee import BoardReferee
from helpers.coordinate import Coordinate
import numpy as np
from tkinter import *


class BoardWidget():
    """docstring for AvalancheGenerator."""

    neighborCoordinates = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def __init__(self, state, master, width, height):
        super().__init__()
        self._state = state
        self._markedMinesCounter = 0
        self._master = master
        self._frameTop = Frame(master, width=width, height=50)
        self._frameTop.pack(side=TOP)
        self._frame = Frame(master, width=width, height=height)
        self._frame.pack()
        self._label = Label(
            self._frameTop,
            text=f'{self._markedMinesCounter}/{self._state.getMinesCount()}',
            fg='red')
        self._label.pack()
        self.mineMarkerImg = PhotoImage(file="game/img/markMine.gif")
        self.mineImg = PhotoImage(file="game/img/mine.gif")
        self.cellOrigImg = PhotoImage(file="game/img/cellOrig.gif")
        self._buttons = np.array([[
            Button(self._frame, image=self.cellOrigImg, width=20)
            for _ in range(self._state.getBoardSize())
        ] for _ in range(self._state.getBoardSize())])

        for i in range(self._state.getBoardSize()):
            for j in range(self._state.getBoardSize()):
                self._buttons[i, j].grid(row=i, column=j)
                self._buttons[i, j].bind("<Button-1>",
                                         lambda event, coord=Coordinate(i, j):
                                         self.leftClick(event, coord))
                self._buttons[i, j].bind("<Button-2>",
                                         lambda event, coord=Coordinate(i, j):
                                         self.rightClick(event, coord))

    def leftClick(self, event, coord):
        cell = self._state.getCell(coord)
        cell.isRevealed = True
        self._buttons[coord.X, coord.Y].config(image='',
                                               width=2,
                                               highlightbackground="#D3D3D3")

        if (cell.isMine):
            self._buttons[coord.X, coord.Y].config(image=self.mineImg,
                                                   width=20)
            self._label.config(text=f'GAME OVER!!!!!!')

        elif (cell.neighborMinesCount == 0):
            neighbors = [
                Coordinate(coord.X + x, coord.Y + y)
                for x, y in self.neighborCoordinates
                if BoardReferee.isOnBoard(coord.X + x, coord.Y +
                                          y, self._state.getBoardSize())
            ]

            for neighbor in neighbors:
                cell = self._state.getCell(neighbor)
                if (not cell.isRevealed and cell.neighborMinesCount == 0):
                    self.leftClick(event, neighbor)
                else:
                    cell.isRevealed = True
                    self._buttons[neighbor.X, neighbor.Y].config(
                        image='', width=2, highlightbackground="#D3D3D3")

        self.redraw()

    def redraw(self):
        for i in range(self._state.getBoardSize()):
            for j in range(self._state.getBoardSize()):
                cell = self._state.getCell(Coordinate(i, j))
                if (cell.isRevealed and cell.neighborMinesCount != 0):
                    self._buttons[i, j].config(text=cell.neighborMinesCount)

    def rightClick(self, event, coord):
        cell = self._state.getCell(coord)
        cell.clickCounter += 1

        if (cell.clickCounter % 2 != 0):
            self._markedMinesCounter += 1
            self._buttons[coord.X, coord.Y].config(image=self.mineMarkerImg,
                                                   width=20)
        else:
            self._markedMinesCounter -= 1
            self._buttons[coord.X, coord.Y].config(image=self.cellOrigImg,
                                                   width=20)

        self._label.config(
            text=f'{self._markedMinesCounter}/{self._state.getMinesCount()}')
        self.redraw()
