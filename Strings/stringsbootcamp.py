# Strings are a special kind of array made out of characters.
# Comparison, joining, splitting, searching for substrings, 
# replacing one string by another, and parsing are all operations
# commonly applied to strings that are not sensible for general arrays,
# so the book has a separate category for them.

# Book example for checking whether a string is palindromic:

def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

# s[~i] is s[-[i + 1]]

print(is_palindromic("sollos"))

# time complexity of O(n) and space complexity of O(1) 
# where n is the length of the string.