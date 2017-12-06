import day4
import unittest

MY_INPUT = "aoc/aoc_2017/data/day4_real.csv"

class Day4Test(unittest.TestCase):

    def test_is_valid_phrase(self):
        self.assertEqual(day4.is_valid_phrase(["aa", "bb", "cc", "dd", "ee"], day4.equals_test), True)
        self.assertEqual(day4.is_valid_phrase(["aa", "bb", "cc", "dd", "aa"], day4.equals_test), False)

    def test_day4_1(self):
        self.assertEqual(day4.day4_1("aoc/aoc_2017/data/day4_1_example.csv"), 1)
        self.assertEqual(day4.day4_1(MY_INPUT), 383)

    def test_day4_2(self):
        self.assertEqual(day4.day4_2("aoc/aoc_2017/data/day4_2_example.csv"), 3)
        self.assertEqual(day4.day4_2(MY_INPUT), 265)

if __name__ == '__main__':
    unittest.main()
