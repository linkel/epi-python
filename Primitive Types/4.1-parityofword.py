# parity is 1 if the number of 1's in the word is odd, otherwise it is 0
# computing the parity of one 64-bit word is straightforward.

# the following counts the bits that are 1 and then modulus by 2 determines odd or even
def computeParity(x):
    num_bits = 0
    while x:
        # this will either add 0 or add 1 depending on the one's place of the other number
        num_bits += x & 1
        # bit shifts over to the right by one, effectively floor dividing by 2
        x >>= 1
    if num_bits % 2 == 0:
        print("number of 1's is even: 0")
    else:
        print("number of 1's is odd: 1")

# the following is the book's example of a brute force algo
# time complexity is O(n) where n is word size
def parity(x):
    res = 0
    # unlike the above, don't bother saving the number of bits that are 1
    # if the bit is 1, then xor that with the result
    # when you hit a 1, that gets xor'd with 0 and result becomes 1
    # if you hit another 1 (even), then 1 ^ 1 becomes 0. 
    # return result
    while x:
        res ^= x & 1
        x >>= 1
    return res

# fun fact: x & (x-1) equals x with its lowest set bit erased.
# for example if x = 00101100, then x-1 = 00101011. therefore x & (x-1) is 00101000.

# that enables the following algorithm to have O(k) runtime,
# where k is the number of bits set to 1 in a particular word.

def kparity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

# what if you compute the parity of a huge number of 64-bit words, though?
# we need to process multiple bits at one time, and cache the results in an array-based lookup table.

# TODO: caching demonstration and masking