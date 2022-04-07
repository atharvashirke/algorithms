import unittest
import sys

sys.path.append("..")

from src.counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):

    def setUp(self):
        self.list = [1, 3, 8, 2, 9 , 2, 5, 6]
        self.max_val = 9
        self.sorted_list = [1, 2, 2, 3, 5, 6, 8, 9]

    def test_simple(self):
        counting_sort(self.list, self.max_val)
        self.assertEqual(self.list, self.sorted_list)


if __name__ == '__main__':
    unittest.main()