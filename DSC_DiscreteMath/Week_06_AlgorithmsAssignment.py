# Algorithm Description

# Inputs: 2 strings
# Output: 1 boolean, describing if the first string is a subsequence of the second

# Steps:
# - Create variable to track how many letters have been matched so far
# - Iterate through the second string (can return early if subsequence is found)
#   - Each time a letter match is found (meaning that the next part of the subsequence has been reached)
#   ... increment the letter-tracking variable.
#     - You find a letter match when the current letter of the second... 
#     ... string (being iterated over) matches the current letter of the first string (indexed using letter-tracking variable)

# At any point if the letter-tracking value matches the length of the subsequence string, it has been found in it's entirety.
# ... meaning that you can return true at that point.

# If the end of the function is reached without having found a complete match, then you can return false.
# Should also handle 0-length strings at start, because algorithm involves iterating over the length.

# ===============================================================
def is_subsequence(sub, containing):
  # Handle edge cases for 0-length inputs
  if (len(sub) == 0):
    return True
  if (len(containing) == 0):
    return False
  
  letters_matched = 0
  for i in range(len(containing)):
    if (containing[i] == sub[letters_matched]):
      letters_matched += 1
      if (letters_matched == len(sub)):
        return True
  return False


string1 = "adce"
string2 = "abcde"

print(str(is_subsequence(string1, string2)))