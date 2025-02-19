import unittest
from age import *

class TestCat_By_AgeFunction(unittest.TestCase):
    def test_child(self):
        self.assertEqual(cat_by_age(0), "Child")
        self.assertEqual(cat_by_age(9), "Child")
    def test_adolescent(self):
        self.assertEqual(cat_by_age(10), "Adolescent")
        self.assertEqual(cat_by_age(18), "Adolescent")
    def test_adult(self):
        self.assertEqual(cat_by_age(19), "Adult")
        self.assertEqual(cat_by_age(65), "Adult")
    def test_golden_age(self):
        self.assertEqual(cat_by_age(66), "Golden age")
        self.assertEqual(cat_by_age(150), "Golden age")
    def test_invalid_age(self):
        self.assertEqual(cat_by_age(-1), "Invalid age:-1")
        self.assertEqual(cat_by_age(151), "Invalid age:151")

if __name__ == "__main__":
    unittest.main()