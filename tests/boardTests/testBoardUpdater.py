import unittest as unittest
from board.boardUpdater import BoardUpdater
from board.state import State
from board.cell import Cell
from helpers.coordinate import Coordinate
from helpers.cellEquals import CellEquals


class Testing_BoardUpdater_With_Board_Size1_And_One_Mine(unittest.TestCase):
    state = State(1, 1)
    sut = BoardUpdater(state)

    def test_update_00_coordinate_should_update_all_neighbors(self):
        self.sut.update(Coordinate(0, 0))
        cell00 = Cell()
        cell00.isMine = True
        cell00.neighborMinesCount = 0

        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 0)), cell00))


class Testing_BoardUpdater_With_Board_Size2_And_One_Mine(unittest.TestCase):
    state = State(2, 1)
    sut = BoardUpdater(state)

    def test_update_00_coordinate_should_update_all_neighbors(self):
        self.sut.update(Coordinate(0, 0))
        cell00 = Cell()
        cell00.isMine = True
        cell00.neighborMinesCount = 0
        cell01 = Cell()
        cell01.isMine = False
        cell01.neighborMinesCount = 1
        cell10 = Cell()
        cell10.isMine = False
        cell10.neighborMinesCount = 1
        cell11 = Cell()
        cell11.isMine = False
        cell11.neighborMinesCount = 1

        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 0)), cell00))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 1)), cell01))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 0)), cell10))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 1)), cell11))


class Testing_BoardUpdater_With_Board_Size2_And_Two_Mines(unittest.TestCase):
    state = State(2, 2)
    sut = BoardUpdater(state)

    def test_update_00_and_11_coordinates_should_update_all_neighbors(self):
        self.sut.update(Coordinate(0, 0))
        self.sut.update(Coordinate(1, 1))
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


class Testing_BoardUpdater_With_Board_Size2_And_Three_Mines(unittest.TestCase):
    state = State(2, 3)
    sut = BoardUpdater(state)

    def test_update_00_01_11_coordinates_should_update_all_neighbors(self):
        self.sut.update(Coordinate(0, 0))
        self.sut.update(Coordinate(0, 1))
        self.sut.update(Coordinate(1, 1))
        cell00 = Cell()
        cell00.isMine = True
        cell00.neighborMinesCount = 2
        cell01 = Cell()
        cell01.isMine = True
        cell01.neighborMinesCount = 2
        cell10 = Cell()
        cell10.isMine = False
        cell10.neighborMinesCount = 3
        cell11 = Cell()
        cell11.isMine = True
        cell11.neighborMinesCount = 2

        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 0)), cell00))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 1)), cell01))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 0)), cell10))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 1)), cell11))


class Testing_BoardUpdater_With_Board_Size3_And_Mine_In_Middle(
        unittest.TestCase):
    state = State(3, 1)
    sut = BoardUpdater(state)

    def test_update_1_1_coordinate_should_update_all_neighbors(self):
        self.sut.update(Coordinate(1, 1))
        cell00 = Cell()
        cell00.isMine = False
        cell00.neighborMinesCount = 1
        cell01 = Cell()
        cell01.isMine = False
        cell01.neighborMinesCount = 1
        cell02 = Cell()
        cell02.isMine = False
        cell02.neighborMinesCount = 1
        cell10 = Cell()
        cell10.isMine = False
        cell10.neighborMinesCount = 1
        cell11 = Cell()
        cell11.isMine = True
        cell11.neighborMinesCount = 0
        cell12 = Cell()
        cell12.isMine = False
        cell12.neighborMinesCount = 1
        cell20 = Cell()
        cell20.isMine = False
        cell20.neighborMinesCount = 1
        cell21 = Cell()
        cell21.isMine = False
        cell21.neighborMinesCount = 1
        cell22 = Cell()
        cell22.isMine = False
        cell22.neighborMinesCount = 1

        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 0)), cell00))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 1)), cell01))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(0, 2)), cell02))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 0)), cell10))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 1)), cell11))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(1, 2)), cell12))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(2, 0)), cell20))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(2, 1)), cell21))
        self.assertTrue(
            CellEquals(self.state.getCell(Coordinate(2, 2)), cell22))
