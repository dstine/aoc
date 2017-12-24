import day16
import test_utils
import unittest

class Day16Test(unittest.TestCase):
    def test_day16_1(self):
        self.assertEqual(day16.day16_1('abcde', test_utils.get_path(__file__, 'day16_example.txt')), 'baedc')
        self.assertEqual(day16.day16_1('abcdefghijklmnop', test_utils.get_path(__file__, 'day16_real.txt')), 'hmefajngplkidocb')

if __name__ == '__main__':
    unittest.main()
