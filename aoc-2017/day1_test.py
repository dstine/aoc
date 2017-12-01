import day1
import unittest

class Day1Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(day1.day1_1("1122"), 3)
        self.assertEqual(day1.day1_1("1111"), 4)
        self.assertEqual(day1.day1_1("1234"), 0)
        self.assertEqual(day1.day1_1("91212129"), 9)
    def test2(self):
        self.assertEqual(day1.day1_2("1212"), 6)
        self.assertEqual(day1.day1_2("1221"), 0)
        self.assertEqual(day1.day1_2("123425"), 4)
        self.assertEqual(day1.day1_2("123123"), 12)
        self.assertEqual(day1.day1_2("12131415"), 4)

if __name__ == '__main__':
    unittest.main()
