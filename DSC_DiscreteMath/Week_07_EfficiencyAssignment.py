# Write step by step Algorithm for Linear Search (finding an element from a list).

# 1. Iterate through list (tracking index with a variable), stopping either when an element is found...
#   ... or when the entire list has been iterated through.
# 2a. If the element was found, return the current index. 
# ... That index represents that the element was found, and is it's position in the list.
# 2b. If the element was NOT found, return a value of -1. 
# ... This value indicates that the value was not found, and is not usable fo indexing the list.

def linearSearch(list, searchElement):
  # 1. Iterate through the list
  for i in range(len(list)):

    # 2a. Element is found, return index.
    if (searchElement == list[i]):
      return i;
  
  # 2b. The failure case
  return -1

# Then, you need to find out the Big O for the program.

# Big-O notation for this program is O(n), because the worst-case search directly correlates to the input list length.