import day3
import unittest

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

if __name__ == '__main__':
    unittest.main()
