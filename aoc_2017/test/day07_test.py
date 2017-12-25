import test_utils
import day07
import unittest

class Day07Test(unittest.TestCase):

    def test_parse_program(self):
        self.assertEqual(
            day07.parse_program(
                "ktlj (57)"),
                {'name': 'ktlj',
                 'weight': 57,
                 'supported_names': [],
                 'supported_weight': 0,
                 'total_weight': 0})
        self.assertEqual(
            day07.parse_program(
                "fwft (72) -> ktlj, cntj, xhth"),
                {'name': 'fwft',
                 'weight': 72,
                 'supported_names': ['ktlj', 'cntj', 'xhth'],
                 'supported_weight': 0,
                 'total_weight': 0})

    def test_day7_1(self):
        self.assertEqual(day07.day7_1(EXAMPLE), 'tknk')
        self.assertEqual(day07.day7_1(MY_INPUT), 'hlqnsbe')

    def test_day7_2(self):
        example = readfile(test_utils.get_path('day7_example.txt'))
        self.assertEqual(day07.day7_2(EXAMPLE), 60)
        self.assertEqual(day07.day7_2(MY_INPUT), 1993)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

EXAMPLE = readfile(test_utils.get_path('day7_example.txt'))
MY_INPUT = readfile(test_utils.get_path('day7_real.txt'))

if __name__ == '__main__':
    unittest.main()
