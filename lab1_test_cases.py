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
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
