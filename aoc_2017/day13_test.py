import day13
import unittest

class Day13Test(unittest.TestCase):
    def test_day13_1(self):
        self.assertEqual(day13.day13_1('aoc/aoc_2017/data/day13_example.txt'), 24)
        self.assertEqual(day13.day13_1(MY_INPUT), 1316)
    def test_day13_2(self):
        self.assertEqual(day13.day13_2('aoc/aoc_2017/data/day13_example.txt'), 10)
        self.assertEqual(day13.day13_2(MY_INPUT), 3840052)

MY_INPUT = 'aoc/aoc_2017/data/day13_real.txt'

if __name__ == '__main__':
    unittest.main()
