import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        #Testing for if the list is empty
        list1 = []
        self.assertEqual(max_list_iter(list1), None)
        #Testing for max as the first number
        list2 = [6, 2, 3, 4]
        self.assertEqual(max_list_iter(list2), 6)
        #Testing for max as the last number
        list3 = [1, 2, 3, 4]
        self.assertEqual(max_list_iter(list3), 4)
        #Testing for max as a middle number
        list4 = [1, 2, 4, 3]
        self.assertEqual(max_list_iter(list3), 4)
        #Testing for max when there are multiple maxes
        list5 = [1, 2, 4, 4]
        self.assertEqual(max_list_iter(list3), 4)

    def test_reverse_rec(self):
        #Testing to see if error is raised
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        #Testing to see if it reverses the List
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        #Testing to see if it finds the target on first try
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )
        #Testing to see if finds target when target is first in list
        self.assertEqual(bin_search(0, low, high, list_val), 0 )
        #Testing to see if target is found when target is last in list
        self.assertEqual(bin_search(10, low, high, list_val), 8 )
        #Testing to see if target is found after many tries and in lower half
        self.assertEqual(bin_search(1, low, high, list_val), 1 )
        #Testing to see if target is found after many tries and in upper half
        self.assertEqual(bin_search(8, low, high, list_val), 6 )
        #Testing to see if target is not in list
        self.assertEqual(bin_search(11, low, high, list_val), None )
        #Testing to see if the error is raised when list is None
        with self.assertRaises(ValueError):
            bin_search(4, low, high, None)
        

if __name__ == "__main__":
        unittest.main()

    
