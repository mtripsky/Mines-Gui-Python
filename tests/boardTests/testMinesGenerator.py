import unittest as unittest
from board.minesGenerator import MinesGenerator
from helpers.coordinate import Coordinate
from helpers.cellEquals import CellEquals


class Testing_MinesGenerator_When_Size_0_Count_0(unittest.TestCase):
    def test_generate_should_return_empty_list(self):
        self.assertTrue(len(MinesGenerator().generate(0, 0)) == 0)


class Testing_MinesGenerator_When_Size_3_Count_0(unittest.TestCase):
    def test_generate_should_return_empty_list(self):
        self.assertTrue(len(MinesGenerator().generate(3, 0)) == 0)


class Testing_MinesGenerator_When_Size_3_Count_3(unittest.TestCase):
    def test_generate_should_return_list_with_three_coordinates(self):
        self.assertTrue(len(MinesGenerator().generate(3, 3)) == 3)


class Testing_MinesGenerator_When_Size_3_Count_20(unittest.TestCase):
    def test_generate_should_return_list_with_nine_coordinates(self):
        self.assertTrue(len(MinesGenerator().generate(3, 20)) == 9)
