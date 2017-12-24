import test_utils
import day14
import unittest

class Day14Test(unittest.TestCase):
    def test_day14_1(self):
        self.assertEqual(day14.day14_1('flqrgnkx'), 8108)
        self.assertEqual(day14.day14_1(MY_INPUT), 8074)

MY_INPUT = 'jzgqcdpd'

if __name__ == '__main__':
    unittest.main()
