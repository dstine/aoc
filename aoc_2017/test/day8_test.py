import test_utils
import day8
import unittest

class Day8Test(unittest.TestCase):
    def test_day8_1(self):
        self.assertEqual(day8.day8_1(EXAMPLE), 1)
        self.assertEqual(day8.day8_1(MY_INPUT), 5966)
    def test_day8_2(self):
        self.assertEqual(day8.day8_2(EXAMPLE), 10)
        self.assertEqual(day8.day8_2(MY_INPUT), 6347)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

EXAMPLE = readfile(test_utils.get_path('day8_example.txt'))
MY_INPUT = readfile(test_utils.get_path('day8_real.txt'))

if __name__ == '__main__':
    unittest.main()
