# A program to count the number of bits that are set to 1 in a positive integer.

def count_bits(x):
    num_bits = 0
    while x:
        # this will either add 0 or add 1 depending on the one's place of the other number
        num_bits += x & 1
        # bit shifts over to the right by one, effectively floor dividing by 2
        x >>= 1
    return num_bits
