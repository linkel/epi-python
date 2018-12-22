# Define a palindromic string to be a string which when
# all the nonalphanumeric are removed it reads the same front to back
# ignoring case. 

# Implement a function which takes as input a string s and returns true
# if s is palindromic

ex = "A man, a plan, a canal, Panama"

# naive approach is to reverse the string, which needs additional space
# proportional to the length of s.

# instead we can traverse the string from right to left,
# using two indices.

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j: # while string char is whitespace
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

print(is_palindrome(ex))
