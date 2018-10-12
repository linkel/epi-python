import math

# Let's say there's a game where you advance through a sequence of positons.
# Each position has a nonnegative integer, representing the max you can advance in one move.
# Start at the first, and win by getting to the last.

A = [2, 4, 1, 1, 0, 2, 3]
B = [3, 3, 1, 0, 2, 0, 1]
C = [3, 2, 0, 0, 2, 0, 1]

# For example in A, you would go one step from A[0] to A[1]. Then go three steps to A[4].
# then 2 steps to A[6] and win. 

# Write a program which takes an array of n integers as above and returns whether it is possible to win.

def game(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    # the furthest index advancable is A[i] + i
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

print(game(A))

# Time complexity is O(n) and additional space used is O(1)

# Write a program to compute the minimum number of steps needed to advance to the last location.

D = [1, 1, 1]
def minimum(A, index = 0):
    last_index = len(A) - 1
    # base case if start and end are same
    if index == last_index:
        return 0
    # if index is 0 then can't go anywhere
    if A[index] == 0:
        return math.inf
    mini = math.inf
    # for the range starting from the next spot of index to the last value in array
    for i in range(index + 1, last_index + 1):
        # if i is smaller or equal to the furthest range it can go
        if (i <= (index + A[index])):
            # recursively call this function to do it again for that next location A[i]
            jumps = minimum(A, i)
            # if what we get back from jumps is not infinite and it is smaller than our minimum, save it
            if ((jumps != math.inf) and (jumps + 1 < mini)):
                mini = jumps + 1
    return mini

print(minimum(A))