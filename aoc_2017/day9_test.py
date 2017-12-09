import day9
import unittest

class Day9Test(unittest.TestCase):
    def test_day9_1(self):
        self.assertEqual(day9.day9_1("{{{}}}"), 6)
        self.assertEqual(day9.day9_1("{{},{}}"), 5)
        self.assertEqual(day9.day9_1("{{{},{},{{}}}}"), 16)
        self.assertEqual(day9.day9_1("{<a>,<a>,<a>,<a>}"), 1)
        self.assertEqual(day9.day9_1("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
        self.assertEqual(day9.day9_1("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
        self.assertEqual(day9.day9_1("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)
        self.assertEqual(day9.day9_1(MY_INPUT), 17537)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

MY_INPUT = readfile('aoc/aoc_2017/data/day9_real.txt')[0]

if __name__ == '__main__':
    unittest.main()
