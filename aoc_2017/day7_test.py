import day7
import unittest

class Day7Test(unittest.TestCase):

    def test_parse_program(self):
        self.assertEqual(
            day7.parse_program("ktlj (57)"),
            ('ktlj', '57', []))
        self.assertEqual(
            day7.parse_program("fwft (72) -> ktlj, cntj, xhth"),
            ('fwft', '72', ['ktlj', 'cntj', 'xhth']))

    def test_day7_1(self):
        example = readfile('aoc/aoc_2017/data/day7_1_example.txt')
        self.assertEqual(day7.day7_1(example), 'tknk')
        self.assertEqual(day7.day7_1(MY_INPUT), 'hlqnsbe')

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

MY_INPUT = readfile('aoc/aoc_2017/data/day7_real.txt')

if __name__ == '__main__':
    unittest.main()
