# Compute X * Y without Arithmetical Operators
# Processors used in very low power devices may not have
# hardware for multiplication, so it must use lower-level primitives.

# Write a program that multiplies two nonnegative integers. 
# Operators allowed to use are assignment, bitwise ops and equality checks/boolean

# Cannot increment/decrement, cannot x < y test

# Can we make an adder first?

def adder(x,y):
    carry = x & y
    res = x ^ y
    while carry != 0:
        shifted_carry = carry << 1
        carry = shifted_carry & res
        res ^= shifted_carry
    return res

print(adder(2,3))

# Can we repeatedly add to multiply? lol

def multiply(x,y):
    count = 1
    res = y
    while count != x:
        res = adder(res, y)
        count = adder(count, 1)
    return res

print(multiply(3,3))  

# Time complexity for the above is osmething like O(2^n) DARN
# n being number of bits in the input. Bah. 
# Multiplication should use shift and add. 

# init result to 0, iterate through bits of x, adding 2^k * y to result
# if the kth bit of x is 1. 
# If you left shift y by k you get 2^k * y. 

# book solution

def multiply2(x,y):
    def add(a,b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >>1)
        return running_sum | carryin
    
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1 # shift x right to get the next bit to look at
        # shift y left because it gets bigger (indent in grade-school mult)
    return running_sum

print(multiply2(3,9))

# why does this work? Fascinating. I tried it a few times and it totally works.
# I did it out on paper a few times--it's just like grade-school multiplication, formalized!
# the 2^k * y thing really confused me but it is really just saying how "indented" it is,
# like the 2^1 = 2 (10), 2^2 = 4 (100), 2^3 = 8 (1000) and that multiplies with y. 

print(int("101101",2))
# checking time 
# import timeit
# res1 =timeit.timeit('multiply(9999,99999)','from __main__ import multiply',number=10)
# res2 =timeit.timeit('multiply2(9999,99999)','from __main__ import multiply2', number=10)

# print(res1,res2)