import aoc_2017.test.test_utils as test_utils
import aoc_2017.day08 as day08
import unittest

class Day08Test(unittest.TestCase):
    def test_day8_1(self):
        self.assertEqual(day08.day8_1(EXAMPLE), 1)
        self.assertEqual(day08.day8_1(MY_INPUT), 5966)
    def test_day8_2(self):
        self.assertEqual(day08.day8_2(EXAMPLE), 10)
        self.assertEqual(day08.day8_2(MY_INPUT), 6347)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

EXAMPLE = readfile(test_utils.get_path('day8_example.txt'))
MY_INPUT = readfile(test_utils.get_path('day8_real.txt'))

if __name__ == '__main__':
    unittest.main()
