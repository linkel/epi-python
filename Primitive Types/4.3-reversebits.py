# Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer
# consisting of the bits of the input in reverse order
# for example, if the input is 111001 then return 100111

# uhh how do I make a lookup table

def bruteforcerev(x):
    for i in range(32):
        bitmask = (1 << i) | (1 << 63 - i)
        x ^= bitmask
    return x

print(bin(bruteforcerev(0b1000101101100101110)))

# okay, so the above only works for exactly 64 bit ints and it takes O(1/2*n) time
# where n is size of word (that's still O(n) lol)

PRECOMPUTED_REVERSE = []
# I still need to learn how to generate a lookup table! book pls

def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE)
            | PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] <<
            (2 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
            | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])