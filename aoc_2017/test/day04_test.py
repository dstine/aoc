import test_utils
import day04
import unittest

MY_INPUT = test_utils.get_path("day4_real.csv")

class Day04Test(unittest.TestCase):

    def test_is_valid_phrase(self):
        self.assertEqual(day04.is_valid_phrase(["aa", "bb", "cc", "dd", "ee"], day04.equals_test), True)
        self.assertEqual(day04.is_valid_phrase(["aa", "bb", "cc", "dd", "aa"], day04.equals_test), False)

    def test_day4_1(self):
        self.assertEqual(day04.day4_1(test_utils.get_path("day4_1_example.csv")), 1)
        self.assertEqual(day04.day4_1(MY_INPUT), 383)

    def test_day4_2(self):
        self.assertEqual(day04.day4_2(test_utils.get_path("day4_2_example.csv")), 3)
        self.assertEqual(day04.day4_2(MY_INPUT), 265)

if __name__ == '__main__':
    unittest.main()
