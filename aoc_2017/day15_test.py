import day15
import unittest

class Day15Test(unittest.TestCase):
    def test_day15_1(self):
        self.assertEqual(day15.day15_1(65, 8921, NUM_PAIRS), 588)
        self.assertEqual(day15.day15_1(516, 190, NUM_PAIRS), 597)

NUM_PAIRS = 40000000

if __name__ == '__main__':
    unittest.main()
