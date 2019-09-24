import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc1
        loc4 = Location("SLO", 35.3, -120.7)
        self.assertFalse(loc1 == loc2)
        self.assertTrue(loc1 == loc4)
        self.assertTrue(loc1 == loc3)
        self.assertFalse(loc2 == loc3)
    def test_init(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc1
        loc4 = Location("SLO", 35.3, -120.7)
        self.assertIsNot(loc1, loc4)
        self.assertIs(loc1, loc3)
        self.assertIsNot(loc1, loc2)
        self.assertIsNot(loc2, loc3)
        self.assertIsNot(loc4, loc2)
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
