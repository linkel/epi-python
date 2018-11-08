# A string over the characters {}()[] is said to be well-formed if the
# different types of brackets match in the correct order.

# Write a program that tests if a string made up of the charcters above
# is well formed.

def is_well_formed(s):
    # here's our stack and the lookup table
    left_chars, lookup = [], {'(':')', '{':'}', '[': ']'}
    for c in s:
        # if character is in the keys of lookup table
        if c in lookup:
            # add it to stack
            left_chars.append(c)
            # if stack is empty, return False since it is not well matched
            # if stack popping and sticking it into the dict finds us our value
            # then we keep going, otherwise returns false
        elif not left_chars or lookup[left_chars.pop()] != c:
            # unmatched
            return False
            # at the end we return True if there's nothing in stack
            # and false if there is stuff left over
    return not left_chars


lookups = {'(':')'}
c = ')'
print(c in lookups)
strings = '(())'
print(is_well_formed(strings))