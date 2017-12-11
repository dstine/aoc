import day11
import unittest

class Day11Test(unittest.TestCase):
    def test_day11_1(self):
        self.assertEqual(day11.day11_1('ne,ne,ne'), 3)
        self.assertEqual(day11.day11_1('ne,ne,sw,sw'), 0)
        self.assertEqual(day11.day11_1('ne,ne,s,s'), 2)
        self.assertEqual(day11.day11_1('se,sw,se,sw,sw'), 3)
        self.assertEqual(day11.day11_1(MY_INPUT), 682)
    def test_day11_2(self):
        self.assertEqual(day11.day11_2(MY_INPUT), 1406)

def readfile(filename):
    with open(filename) as file:
        line = file.readline()
        return line

MY_INPUT = readfile('aoc/aoc_2017/data/day11_real.txt')

if __name__ == '__main__':
    unittest.main()
