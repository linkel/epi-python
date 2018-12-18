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
    
