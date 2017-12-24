import test_utils
import day6
import unittest

MY_INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

class Day6Test(unittest.TestCase):

    def test_day6_1(self):
        self.assertEqual(day6.day6_1([0, 2, 7, 0]), 5)
        self.assertEqual(day6.day6_1(MY_INPUT), 6681)

    def test_day6_2(self):
        self.assertEqual(day6.day6_2([0, 2, 7, 0]), 4)
        self.assertEqual(day6.day6_2(MY_INPUT), 2392)

if __name__ == '__main__':
    unittest.main()
