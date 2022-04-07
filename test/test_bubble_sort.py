import unittest
import sys

sys.path.append("..")

from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.list = [1, 3, 8, 2, 9 , 2, 5, 6]
        self.sorted_list = [1, 2, 2, 3, 5, 6, 8, 9]

    def test_simple(self):
        bubble_sort(self.list)
        self.assertEqual(self.list, self.sorted_list)


if __name__ == '__main__':
    unittest.main()