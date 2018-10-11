# Input: an array of integers
# Reorder its entries so that even entries appear first.
# O(n) space where n is length of array solution is trivial: also solve without allocating additional storage.

example = [2,3,4,5,8,13,15,16]

# expected: [16, 8, 4, 2, 3, 5, 13, 15]
# Any order is fine as long as even entries are before the odd entries.

def trivial(A):
    B = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            B.insert(0,A[i])
        else:
            B.append(A[i])  
    return B

print(trivial(example))

# the above is the O(n) space usage example because a new list is initialized.
# the new list takes up equivalent space to the original array.
# how about an O(1) space solution?
# partition the array into three sections: even, unclassified, and odd.
# even and odd are empty and unclassified takes up the whole array at first.
# as we iterate through unclassified, the elements get moved to the boundaries via swaps.

examplecopy = [2,3,4,5,8,13,15,16]

def even_odd(A):
    # setting the even boundary to the start and the odd to the end of the array
    next_even, next_odd = 0, len(A) - 1
    # iterates from start to end
    while next_even < next_odd:
        # if the number in that index is even, don't move it and move boundary to the next one
        if A[next_even] % 2 == 0:
            next_even += 1
        # if the number in that index is odd, we swap it with the one at the boundary of the odds and smallen the boundary
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

even_odd(examplecopy)
print(examplecopy)