# Write a program that performs base conversion. The input is a string,
# an integer b1 that represents the base of the string, and another integer b2. The output should be the string
# representing the integer in base 2. 

# Example in base 10:
# 314 is the number 3x100 + 1x10 + 4x1.
#  

import string
import functools

def convert_base(stringg, b1, b2):
    def construct(integer, base):
        return ('' if integer == 0 else
                construct(integer//base, base) +
                string.hexdigits[integer % base].upper())
    is_negative = (stringg[0] == '-')
    integer = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        stringg[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if integer == 0 else
                                           construct(integer, b2))

thestring = "615"
print(convert_base(thestring, 7, 13))
    
# time complexity is O(n(1+log(baseb2)b1)) where n is length of string.
# You do n multiply-and-adds to get x from s, then we multiply and add by log base b2 x times,
# to get the result. 

# need to revisit this