# Implement code that takes as input a 64-bit integer and swaps the bits at
# indices i and j (the most significant bit and the least significant bit).

def bruteswap(x, i, j):
    bitmask = (1 << i) | (1 << j)
    print(bitmask)
    x = x ^ bitmask
    return x

print(bruteswap(16, 4, 9))

# check if the bits are identical first
def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        print(bit_mask)
        x ^= bit_mask
    return x

print(swap_bits(16, 4, 9))

#print(bin(16))

# Time complexity is O(1).

# the above give different results if the indices are out of range sometimes
# because the brute force one doesn't check, so if the index is out of range
# it will end up xor'ing the result anyway
# while for the other one it won't xor it unless the bits are different
# so the only time when it gives the same result for an index out of range
# will be when you use a location with a 1 for one index and then
# go out of bounds with the other.