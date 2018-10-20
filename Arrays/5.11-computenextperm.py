# Write a program that takes as input a permutation, and returns
# the next permutation under dictionary ordering.
# If the permutation is the last permutation return empty array.
# i.e., if input [1, 0, 3, 2] return [1, 2, 0, 3]
# Dictionary ordering is defined as p appears before q if 
# starting from index 0 the corresponding entry for p is
# less than that of q. so [2, 0, 1] is < [2, 1, 0]

# 0 1 2, 0 2 1, 1 0 2, 1 2 0, 2 0 1, 2 1 0, []

A = [2, 0, 1]
def nextPerm(P):
    inversionPt = len(P) - 2
    while (inversionPt >= 0 and P[inversionPt] >= P[inversionPt + 1]):
        inversionPt -= 1
    if inversionPt == -1:
        return []
    for i in reversed(range(inversionPt + 1, len(P))):
        if P[i] > P[inversionPt]:
            P[inversionPt], P[i] = P[i], P[inversionPt]
            break
    P[inversionPt + 1:] = reversed(P[inversionPt + 1:])
    return P

print(nextPerm(A))

# I need to read this over again. I am not sure I completely get it. 
# 10-19-2018