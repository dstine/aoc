import aoc_2017.day15 as day15
import unittest

class Day15Test(unittest.TestCase):
    def test_day15_1(self):
        num_pairs = 40000000
        self.assertEqual(day15.day15_1(65, 8921, num_pairs), 588)
        self.assertEqual(day15.day15_1(516, 190, num_pairs), 597)
    def test_day15_2(self):
        num_pairs = 5000000
        self.assertEqual(day15.day15_2(65, 8921, num_pairs), 309)
        self.assertEqual(day15.day15_2(516, 190, num_pairs), 303)

if __name__ == '__main__':
    unittest.main()
