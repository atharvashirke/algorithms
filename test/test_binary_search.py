import unittest
import sys

sys.path.append("..")

from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.sorted_list = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

    def test_simple(self):
        target = 4
        self.assertEquals(binary_search(self.sorted_list, target), 1)


if __name__ == '__main__':
    unittest.main()
