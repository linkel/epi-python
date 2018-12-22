# Spreadsheets use an alphabetical encoding of 
# successive columns. Like A, B, C....Y, X, AA, AB...ZZ, AAA, AAB
# Convert a spreadsheet column id to the corresponding integer, with "A"
# corresponding to 1. 

import string
import functools

# in progress! trying to write one
def convert(spreadsheet_id):
    lookup = {}
    digit = 1
    for letter in string.ascii_uppercase:
        lookup[letter] = digit
        digit += 1
    unit = 0
    final = 0
    for char in spreadsheet_id[-1::-1]:
        correspond = lookup[char]
        final += correspond*(26**unit)
        unit += 1
    return final

print(convert("AAA"))


# book solution

def ss_decode_col_id(col):
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord("A") + 1, col, 0)

# book notes that you could enumerate all of the column ids and stop when
# the id equals the input. This would take 26^6 steps to get to ZZZZZZ,
# so the complexity is O(26^n) where n is the length of the string. Bad!
# 
# So really this problem is really just the conversion of a base-26 number
# into the integer, with A being 1 instead of 0. 
# 
   
# time complexity of book solution is O(n) and it doesn't use additional space like mine.

# Variant: solve same problem with A corresponding to 0.

# modifying my own solution...I'm at a loss as to the book's solution for modification
def convertA0(spreadsheet_id):
    lookup = {}
    digit = 0
    for letter in string.ascii_uppercase:
        lookup[letter] = digit
        digit += 1
    unit = 0
    final = 0
    for char in spreadsheet_id[-1::-1]:
        correspond = lookup[char]
        if correspond != 0:
            final += correspond*(26**unit)
        else:
            final += (26**unit)
        unit += 1
    return final

# Implement a function that converts an integer to the spreadsheet column id:

def convertInt(myInt):
    lookup = {}
    digit = 0 # will never have a 26 here from remainder so gotta start from 0
    for letter in string.ascii_uppercase:
        lookup[digit] = letter
        digit += 1
    div = myInt
    result = ''
    while div != 0:
        rem = (div-1) % 26
        result = result + lookup[rem]
        div = (div-rem) // 26        
    return result

print(convertInt(702))
