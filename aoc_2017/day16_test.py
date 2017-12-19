import day16
import unittest

class Day16Test(unittest.TestCase):
    def test_day16_1(self):
        self.assertEqual(day16.day16_1('abcde', 'aoc/aoc_2017/data/day16_example.txt'), 'baedc')
        self.assertEqual(day16.day16_1('abcdefghijklmnop', 'aoc/aoc_2017/data/day16_real.txt'), 'hmefajngplkidocb')

if __name__ == '__main__':
    unittest.main()
