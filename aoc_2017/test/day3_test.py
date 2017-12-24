import test_utils
import day3
import unittest

MY_INPUT = 368078

class Day3Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(day3.day3_1(1), 0)
        self.assertEqual(day3.day3_1(2), 1)
        self.assertEqual(day3.day3_1(3), 2)
        self.assertEqual(day3.day3_1(9), 2)
        self.assertEqual(day3.day3_1(10), 3)
        self.assertEqual(day3.day3_1(12), 3)
        self.assertEqual(day3.day3_1(23), 2)
        self.assertEqual(day3.day3_1(1024), 31)
        self.assertEqual(day3.day3_1(MY_INPUT), 371)
    def test2(self):
        self.assertEqual(day3.day3_2(30), 54)
        self.assertEqual(day3.day3_2(MY_INPUT), 369601)

if __name__ == '__main__':
    unittest.main()
