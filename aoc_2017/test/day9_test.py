import test_utils
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
    def test_day9_2(self):
        self.assertEqual(day9.day9_2("<>"), 0)
        self.assertEqual(day9.day9_2("<random characters>"), 17)
        self.assertEqual(day9.day9_2("<<<<>"), 3)
        self.assertEqual(day9.day9_2("<{!>}>"), 2)
        self.assertEqual(day9.day9_2("<!!>"), 0)
        self.assertEqual(day9.day9_2("<!!!>>"), 0)
        self.assertEqual(day9.day9_2('<{o"i!a,<{i<a>'), 10)
        self.assertEqual(day9.day9_2(MY_INPUT), 7539)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

MY_INPUT = readfile(test_utils.get_path('day9_real.txt'))[0]

if __name__ == '__main__':
    unittest.main()
