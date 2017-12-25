import test.test_utils as test_utils
import day12
import unittest

class Day12Test(unittest.TestCase):
    def test_day12_1(self):
        self.assertEqual(day12.day12_1(test_utils.get_path('day12_example.txt')), 6)
        self.assertEqual(day12.day12_1(MY_INPUT), 288)
    def test_day12_2(self):
        self.assertEqual(day12.day12_2(test_utils.get_path('day12_example.txt')), 2)
        self.assertEqual(day12.day12_2(MY_INPUT), 211)

MY_INPUT = test_utils.get_path('day12_real.txt')

if __name__ == '__main__':
    unittest.main()
