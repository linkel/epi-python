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

# Let's start with an example using a 2 bit word.
# parities of 00, 01, 10, and 11 are [0, 1, 1, 0]
precomputed = [0, 1, 1, 0]

def parity2bit(x):
    MASK_SIZE = 2 # 2 bit words, up tp 8 bit int
    BIT_MASK = 0b0011
    return (precomputed[x >> (3*MASK_SIZE)] ^
            precomputed[(x >> (2*MASK_SIZE)) & BIT_MASK] ^
            precomputed[(x >> MASK_SIZE) & BIT_MASK] ^
            precomputed[x & BIT_MASK])

#print(parity2bit(8))

precomputed64 = []
# I need to figure out how to generate a lookup table.

def parity64bit(x):
    MASK_SIZE = 16 # 16 bit words, up to 64 bit int
    BIT_MASK = 0xFFFF # F in hex indicates four bits of 1
    return (precomputed64[x >> (3*MASK_SIZE)] ^
            precomputed64[(x >> (2*MASK_SIZE)) & BIT_MASK] ^
            precomputed64[(x >> MASK_SIZE) & BIT_MASK] ^
            precomputed64[x & BIT_MASK])

# time complexity of the above is a function of the size of the keys
# used to index the lookup table. 
# If L is the width of the words for which we cache the results, and n the word size
# then there are n/L (word size div by width of word) terms.
# The time complexity is then O(n/L) assuming that shifting takes O(1)
# DOES NOT INCLUDE the initialization time of the lookup table.

# Can use XOR to make this speedier. XOR of a group of bits is its parity.
# like if we have 64 bits and cut them in half and XOR 'em together,
# only stuff that did not match up is left.
# then we can keep dividing in in half and XOR'ing it until it's one bit. 

# may need to extract the result from the least significant bit at the end.
# in which case you can bitwise AND with the size of the word with a 1 in the least sig place.

def xorParity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

# time complexity is O(logn) where n is word size due to the DIVIDIN'.

# Can combine caching with word-level ops. For example,
# could do the xor until 16 bits then do the lookup.
# speed depends on input data.
# supposedly the brute force approach above gets 20% faster with the x & x - 1 trick
# and then the table lookup is 4x faster and the associativity of the xor part 
# makes it another 2x faster.

# Write expressions that use bitwise ops, equality checks, and bools to
# do the following in O(1) time:

# Right propagate the rightmost set bit in x, e.g., 01010000 to 01011111

def rightPropagate(x):
    isolate = (x & ~(x - 1))
    complement = ~isolate & 0xF
    return (x + complement)

#print(rightPropagate(0b01010000))
#print(bin(95))
# the above works for up to 4 bits to propagate. I wonder how to do better?
# the two's complement thing is really throwing me off.

# oh my fuggin god it's super simple

def rightmostPropagate(x):
    return x | x - 1 

#print(rightmostPropagate(0b01010000))

# Compute x mod a power of 2, for example returns 13 for 77 mod 64 
# not sure I totally get it. remainder from any power of 2 number?

x = 7
powerof2 = 4
def power2mod(x,powerof2):
    return x & (powerof2 -1)

print(power2mod(x, powerof2))

# Okay, so the trick is that powers of 2 are always 1 with zeroes after.
# like how 2 is 10, 4 is 100, 8 is 1000. 
# so if you subtract 1 from it, it becomes all 1s.
# then you can AND it with the number to get those remaining 1s.
# Did not come up with this on my own.

# Test if x is a power of 2, true if so, and false for all others.

def testif(x):
    if x == (x & ~(x-1)):
        return True
    else:
        return False

print(testif(128))

# this just tests whether isolating that first set bit is the same as the 
# number itself. since 0b1000 subtracted by one is 0b0111 and the complement
# of it is also 0b1000 then they're the same as the original and it's True.

print(~0b1000)
print(bin(-9))

# this two's complement stuff is still puzzling me.
# why the heck is the complement of 8, -9?
# I thought if 0b1000 gets ~'d it becomes 0b011, which is 7. I just want to keep that 7.
# the two's complement thing flips it again back to 1000 then adds 1???
# have to mask to keep the 7. Need to review this later.