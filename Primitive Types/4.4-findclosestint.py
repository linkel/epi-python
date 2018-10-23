# Find a closest integer with the same weight.
# Define the weight of a nonnegative integer x to be the number of 
# bits that are set to 1 in the binary representation.
# Ex: Since 92 is binary is 1011100, the weight of 92 is 4.

# Write a program that takes a nonenegative integer x and returns a number y
# which is not equal to xbut has the same weight as x and their 
# difference, abs(y - x) is as small as possible. 

# So the brute force approach of trying all integers is pretty bad. 
# For some inputs it'd have to evaluate over one billion integers. 

# It might be appealing to swap the least significant bit with the right most
# bit that differs with it. It will not work across all inputs. (111 to 1110)

# swap the two rightmost consecutive bits that differ is the best approach

def closestInt(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1)) #swaps bit-i and bit - (i + 1)
            return x
    raise ValueError('All bits are 0 or 1')

# Time complexity is O(n) where n is the integer width.

# Solve the same problem in O(1) time and space. 