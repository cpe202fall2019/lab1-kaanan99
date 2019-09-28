import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        #Making the default object
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        #Creating a different object
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc1
        loc4 = Location("SLO", 35.3, -120.70000001)
        loc5 = Location("SLO", 35.3, -120.7)
        loc6 = Location("SF", 35.3, -120.7)
        #Testing to see if two different objects are equal
        self.assertFalse(loc1 == loc2)
        #Testing to see if a refrence to the same object is equal
        self.assertTrue(loc1 == loc3)
        #Testing to see if two identical objects are equal
        self.assertTrue(loc1 == loc5)
        #Testing for different types
        self.assertFalse(loc1 == "hi")
        #Testing for rounding
        self.assertTrue(loc1 == loc4)
        #Testing for different name
        self.assertFalse(loc1 == loc6)
        
        
    def test_init(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc1
        loc4 = Location("SLO", 35.3, -120.7)
        #To see if two different objects are the same
        self.assertIsNot(loc1, loc4)
        #To see if a refrence to same object is the same
        self.assertIs(loc1, loc3)
        #To see if different objects with different info are the same
        self.assertIsNot(loc1, loc2)
        #To see if object and refrence to difference object are the same
        self.assertIsNot(loc2, loc3)
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
