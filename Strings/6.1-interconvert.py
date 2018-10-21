import functools
import string

# Take a string representing an integer and return the corresponding
# integer, and vice versa. Handle negative integers.
# Do not use library functions like int(). 

stringA = "143"
intA = 143

def intToString(x):
    newString = []
    isNegative = False
# 48 to 57 is 0 to 9 in ascii
    if x < 0:
        isNegative = True
        x = -x
    while x != 0:
        current = x % 10
        newString.append(chr(ord('0') + current))
        x = x // 10
    return ('-' if isNegative else '') + ''.join(reversed(newString))

print(intToString(intA))

# Book solution for String to Integer

def string_to_int(s):
    return functools.reduce( lambda running_sum, c: running_sum * 10 + string.digits.index(c),
    s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

print(string_to_int(stringA))