# Let an array P specify a permutation where P[i] represents the location
# of element at i in the permutation. 

# Given an array A of n elements and a permutation P, apply P to A.

A = [0, 1, 2, 3, 4]
P = [4, 2, 3, 1, 0]

def applyPermute(A, P):
    newArray = [0] * len(P)
    for i in range(len(P)):
        newArray[P[i]] = A[i]
    return newArray

print(applyPermute(A, P))

# Using additional space makes it simple to solve this problem.
# But that's a time complexity of O(n) and a space complexity of O(n).
# Improving space complexity here can involve decomposing
# permutations into simpler structures.
# Because permutations can be represented by a collection of 
# independent permutations each of which are cyclic.

B = [0, 1, 2, 3, 4]

def apply_permutation(P, A):
    for i in range(len(A)):
        next = i
        while P[next] >= 0:
            A[i], A[P[next]] = A[P[next]], A[i]
            temp = P[next]
            P[next] -= len(P)
            next = temp
    # restore permutation
    P[:] = [a + len(P) for a in P]

print(apply_permutation(P, B))
print(B)

# the above is O(n) time and O(1) space, using the sign of the permutation
# to determine whether it has already been edited.

# can also go left to right 

def applyPermLR(P, A):
    def cyclicPerm(start, P, A):
        i, temp = start, A[start]
        while True:
            next_i = P[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break
    for i in range(len(A)):
        j = P[i]
        while j != i:
            if j < i:
                break
            j = P[j]
        else:
            cyclicPerm(i, P, A)

applyPermLR(P, A)
print(A)

# Given an array A of integers representing a permutation, update A to
# represent the inverse permutation using only constant additional storage

