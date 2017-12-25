import test.test_utils as test_utils
import day13
import unittest

class Day13Test(unittest.TestCase):
    def test_day13_1(self):
        self.assertEqual(day13.day13_1(test_utils.get_path('day13_example.txt')), 24)
        self.assertEqual(day13.day13_1(MY_INPUT), 1316)
    def test_day13_2(self):
        self.assertEqual(day13.day13_2(test_utils.get_path('day13_example.txt')), 10)
        self.assertEqual(day13.day13_2(MY_INPUT), 3840052)

MY_INPUT = test_utils.get_path('day13_real.txt')

if __name__ == '__main__':
    unittest.main()
