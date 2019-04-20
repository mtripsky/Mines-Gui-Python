import unittest2 as unittest
from unittest.mock import MagicMock
from board.boardInitializer import BoardInitializer
from board.boardUpdater import BoardUpdater
from board.state import State
from board.cell import Cell
from helpers.coordinate import Coordinate
from helpers.cellEquals import CellEquals


class Testing_BoardInitializer_With_Board_Size2_And_No_Mines(
        unittest.TestCase):
    state = State(2, 0)
    mock = MagicMock()
    mock.generate.return_value = []
    updater = BoardUpdater(state)

    sut = BoardInitializer(state, mock, updater)

    def test_initialize_board_with_2_mines_should_not_update_anything(self):
        self.sut.initiate()
        cell00 = Cell()
        cell01 = Cell()
        cell10 = Cell()
        cell11 = Cell()

        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 0)), cell00))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 1)), cell01))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 0)), cell10))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 1)), cell11))


class Testing_BoardInitializer_With_Board_Size2_And_Two_Mines(
        unittest.TestCase):
    state = State(2, 2)
    mock = MagicMock()
    mock.generate.return_value = [Coordinate(0, 0), Coordinate(1, 1)]
    updater = BoardUpdater(state)

    sut = BoardInitializer(state, mock, updater)

    def test_initialize_board_with_2_mines_at_00_and_11_should_update_all_neighbors(
            self):
        self.sut.initiate()
        cell00 = Cell()
        cell00.isMine = True
        cell00.neighborMinesCount = 1
        cell01 = Cell()
        cell01.isMine = False
        cell01.neighborMinesCount = 2
        cell10 = Cell()
        cell10.isMine = False
        cell10.neighborMinesCount = 2
        cell11 = Cell()
        cell11.isMine = True
        cell11.neighborMinesCount = 1

        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 0)), cell00))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 1)), cell01))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 0)), cell10))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 1)), cell11))
