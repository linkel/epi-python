# Given an unsorted collection of n keys, we will have to examine each element to find the one we want.
# We know that's got O(n) complexity.
# But if we have a sorted array, we can do this in O(log n). 
# Though the sorting itself would have taken O(n log n) time...
# But if we do a ton of searches compared to sorting then it's worth it. 

# So in binary search, you can look at an element in the middle of this sorted list
# And if we know our element's gonna be bigger, we eliminate the other half and do it again.

# Divide and conquer and all that. 

# time complexity of binary search is given by T(n) = T(n/2) + c. 

# returns -1 if not found
def bsearch(element, arr):
    lower, upper = 0, len(arr) - 1
    while lower <= upper:
        # this was done instead of just upper + lower // 2
        # because in a language with potential to overflow (not Python lol)
        # the sum of lower and upper could be way too big
        midpoint = lower + (upper - lower) // 2
        if arr[midpoint] < t:
            lower = midpoint + 1
        elif arr[midpoint] == element:
            return midpoint
        else: 
            upper = midpoint - 1
    return -1

