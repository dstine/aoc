import day10
import unittest

class Day10Test(unittest.TestCase):
    def test_day9_1(self):
        self.assertEqual(day10.day10_1(5, '3, 4, 1, 5'), 12)
        self.assertEqual(day10.day10_1(256, MY_INPUT), 6909)

def readfile(filename):
    with open(filename) as file:
        line = file.readline()
        return line

MY_INPUT = readfile('aoc/aoc_2017/data/day10_real.txt')

if __name__ == '__main__':
    unittest.main()
