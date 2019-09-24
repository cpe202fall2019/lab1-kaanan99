
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   elif len(int_list) == 0:
      return None
   max = int_list[0]
   for n in int_list:
      if n > max:
         max = n
   return max
   
def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   new = []
   new.append(int_list[0])
   if len(int_list) == 1:
      return new
   else:
      return reverse_rec(int_list[1:]) + new

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   high = int_list.index(int_list[high])
   if (high - low) % 2 == 0:
      mid = int(low +((high - low) / 2))
   else:
      mid = int(low + (((high - low) / 2) - .5))
   if target == int_list[mid]:
      return mid
   if high - low == 0 and high - low != target:
      return None
   elif target > int_list[mid]:
      return bin_search(target, int(mid + 1), high, int_list)
   else:
      return bin_search(target, low, int(mid - 1), int_list)
