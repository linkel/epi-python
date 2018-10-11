# Write a program that takes an array A and an index i into A, and
# rearranges the elements such that all elements less than A[i] (the pivot)
# appear first, followed by elements equal, then elements greater. 

# The problem is trivial with O(n) additional space, where n is the length of A.

# example lazy solution (wastes time going through array twice)

A = [0, 1, 2, 0, 2, 1, 1]
B = [9, 3, 1, 6, 3, 2, 3, 6, 9, 4]

def sortA(A, pivot_index):
    pivot = A[pivot_index]
    newList = []
    for item in A:
        if item < pivot:
            newList.insert(0, item)
        elif item == pivot:
            newList.append(item)
    for item in A:
        if item > pivot:
            newList.append(item)
    return newList

#print(sortA(A,1))
#print(sortA(B,3))

# another lazy solution goes through array once but makes three sublists

def sortB(A, pivot_index):
    pivot = A[pivot_index]
    smallList = []
    equalList = []
    bigList = []
    for item in A:
        if item < pivot:
            smallList.append(item)
        elif item == pivot:
            equalList.append(item)
        elif item > pivot:
            bigList.append(item)
    return smallList + equalList + bigList

#print(sortB(B,4))

# How may we avoid using additional space?

def dutchflag(A, pivot_index):
    pivot = A[pivot_index]
    # First pass: group elements smaller than the pivot
    for i in range(len(A)):
        # look for smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements bigger than pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


# the above solution now uses O(1) space, but it uses O(n^2) time complexity! 
# let's have something that is O(n) time.
# the following removes the repeated additional element search.

def dutchflag2(A, pivot_index):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # smaller serves as our index here
    # Second pass: group larger elements
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

# what about a way that uses even less time? The above was something like 2n. Let's do n.

def dutchflag3(A, pivot_index):
    pivot = A[pivot_index]
    # separate into four groups
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    # as long as unclassified element exists, keep iterating
    while equal < larger:
        # starting from the beginning, which is unclassified to start off
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: 
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

# assuming that keys take one of three values, reorder the array so that all obj with same key
# appear together. Use O(1) additional space and O(n) time.
# I'm going to be lazy and use the pivot idea from above...

C = [1, 2, 1, 1, 0, 0, 2, 0, 2]

def reorder(A):
    # let's try having four categories again. 0, 1, 2, and unclassified.
    zeroes, ones, twos = 0, 0, len(A)
    while ones < twos:
        if A[ones] < 1:
            A[zeroes], A[ones] = A[ones], A[zeroes]
            zeroes, ones = zeroes + 1, ones + 1
        elif A[ones] == 1:
            ones += 1
        else:
            twos -= 1
            A[ones], A[twos] = A[twos], A[ones]

reorder(C)
print(C)

# given an array A of n objects with keys that takes one of four values, reorder the array so that all obj 
# that have the same key appear together.

# can I just apply the pivot idea again?

D = [1, 2, 3, 0, 3, 0, 3, 1, 2, 0, 2, 1]

def reorderfour(A):
    zeroes, ones, twos, threes = 0, 0, 0, len(A)
    while twos < threes:
        if A[twos] < 2:
            A[ones], A[twos] = A[twos], A[ones]
            ones, twos = ones + 1, twos + 1
        elif A[twos] == 2:
            twos += 1
        else:
            threes -= 1
            A[twos], A[threes] = A[threes], A[twos]
    print(zeroes)
    print(ones)
    print(twos)
    while zeroes < ones:
        if A[ones] < 1:
            A[zeroes], A[ones] = A[ones], A[zeroes]
            zeroes += 1
        else:
            ones -= 1

reorderfour(D)
print(D)

# given an array A of n objects with boolean-valued keys, reorder the array so that obj 
# with the key false appear first.

E = [True, False, False, True, True, False]

def reorderBool(A):
    falses, trues = 0, len(A)
    while falses < trues:
        if A[falses] == False:
            falses += 1
        elif A[falses] == True:
            trues -= 1
            A[falses], A[trues] = A[trues], A[falses]


reorderBool(E)
print(E)

# given an array A of n objects with Boolean-valued keys, reorder the array so that objects that have the key false
# appear first. relative ordering of objects with key true should not change.

# TODO: answer