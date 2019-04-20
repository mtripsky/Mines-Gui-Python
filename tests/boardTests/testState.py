import unittest as unittest
from board.state import State
from board.cell import Cell
from helpers.coordinate import Coordinate
from helpers.cellEquals import CellEquals


class Testing_State_With_Board_Size2_And_Zero_Mines(unittest.TestCase):
    sut = State(2, 0)

    def test_getCell(self):
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(0, 0)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(0, 1)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(1, 0)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(1, 1)), Cell()))

    def test_BoardSize_should_return_2(self):
        self.assertEqual(2, self.sut.getBoardSize())

    def test_MinesCount_should_return_0(self):
        self.assertEqual(0, self.sut.getMinesCount())


class Testing_State_With_Board_Size3_And_3_Mines(unittest.TestCase):
    sut = State(3, 3)

    def test_getCell(self):
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(0, 0)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(0, 1)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(0, 2)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(1, 0)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(1, 1)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(1, 2)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(2, 0)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(2, 1)), Cell()))
        self.assertTrue(CellEquals(self.sut.getCell(Coordinate(2, 2)), Cell()))

    def test_BoardSize_should_return3(self):
        self.assertEqual(3, self.sut.getBoardSize())

    def test_MinesCount_should_return_3(self):
        self.assertEqual(3, self.sut.getMinesCount())
