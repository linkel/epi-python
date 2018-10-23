# Implement an algorithm that takes as input an array of distinct
# elements and a size, and returns a subset of
# the given size of the array elements. All subsets should be
# equally likely. Return result in input array.

import random

def random_sampling(k, A):
    for i in range(k):
        # generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

# time complexity is O(k) to select the elements
# runs in O(1) space

