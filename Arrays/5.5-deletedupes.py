# Write a program which takes as input a sorted array and updates it so that all duplicates
# are removed and the remainng elements shifted left to fill the emptied indices
# return the # of valid elements. After the last valid entries you can leave the values stored beyond it as is.
# no libraries allowed.

A = [2, 3, 4, 4]
B = [2, 3, 5, 5, 7, 11, 11, 11, 13]

# the following solution uses O(n) additional space where n is the size of the array
# it also uses O(n) time complexity since it needs to go thru the list
# but this doesn't actually answer the question...can't return number of valid elements
# since I am returning the new array instead. 

def deleteDupes(A):
    newList = []
    for i in A:
        if i not in newList:
            newList.append(i)
    return newList

# to make it work according to the question, can copy list into A
# book says to use hashtable for unique vals...is this okay instead?

def deleteDupesProper(A):
    newList = []
    for i in A:
        if i not in newList:
            newList.append(i)
    valid = len(newList)
    for i in range(len(newList)):
        A[i] = newList[i]
    return valid

print(deleteDupesProper(A))
print(A)
# Let's try an O(1) space solution.
# this is a brute force solution that iterates through the array and takes out values that are dupes
# it inserts empty strings at the beginning so as to not affect the index
# then removes the empty strings at the end.
# time complexity I think is O(n) but with a multiplier, maybe 2n + the operations of unnecessary inserting.

def deleteDuplicatesbf(A):
    current = None
    startinglength = len(A)
    for i in range(len(A)):
        if current != A[i]:
            current = A[i]
        elif current == A[i]:
            A.remove(current)
            A.insert(0, '')
    removed = A.count('')
    for i in range(removed):
        A.remove('')
    return (startinglength - removed)
                
#print(deleteDuplicatesbf(B))
#print(B)

# one can also have a O(n^2) brute force solution that shifts elements to the left by one
# if they are not equal. I think this solution is worse than the one I wrote above.

# If we want good time complexity, we can reduce the amount of shifting.

C = [3, 3, 4, 6, 7, 7, 8, 9, 9]
D = [2, 3, 5, 5]
E = [2, 3, 5, 5, 6]

def delete_duplicates(A):
    if not A:
        return 0
    index = 1
    for i in range(1, len(A)):
        if A[index - 1] != A[i]:
            A[index] = A[i]
            index += 1
    return index

#print(C)
#print(delete_duplicates(C))
#print(C)

# in the following test case, there are only three valid elements
# as per the question, the values stored beyond the valid elements we don't care about

#print(D)
#print(delete_duplicates(D))
#print(D)

# and if there is stuff after, the last value can just stay

#print(E)
#print(delete_duplicates(E))
#print(E)

# Implement a fn that takes as input an array and a key and updates the array
# so that all occurrences of the key have been removed
# and the remaining elments are shifted left to fill the empty indices
# return the remaining elements. No requirements to the values stored beyond the last valid element.
C = [3, 3, 4, 6, 7, 7, 8, 9, 9]
key = 7
def deleteKey(A, key):
    if not A:
        return 0
    index = 0
    for i in range(1, len(A)):
        if A[index] != key:
            index += 1
        if A[index] == key and A[i] != key:
            A[index] = A[i]
            index += 1
    return index

print(deleteKey(C, key))
print(C)

# well, I'm not leaving the list in sorted form here...
# how can we keep the list sorted?

F = [6, 7, 8, 9, 7, 9]
key = 7
def deleteKeysorted(A, key):
    if not A:
        return 0
    index = 0
    deleted = 0
    for i in range(1, len(A)):
        if deleted > 0 and A[i] != key:
            A[index] = A[i]
        if A[index] != key:
            index += 1
        elif A[index] == key and A[i] != key:
            A[index] = A[i]
            index += 1
            deleted += 1
    return index

print(deleteKeysorted(F, key))
print(F)

# well, this keeps the list sorted. If stuff gets deleted we move everything unless it's the key
# that we keep all instances of the key out of the list. Even though the book says there are no req
# to the values stored beyond the last valid, I kinda think leaving the key in there past the valid area
# is still incorrect. 

# Write a program which takes as input a sorted array A of integers and a positive integer m,
# and updates A so that if x appears m times in A it appears exactly min(2, m) times in A.
# perform update in one pass and no additional storage may be allocated.

# The below does not work correctly yet. Need to come back to it.

G = [1, 2, 2, 2, 2, 9, 9]
m = 4

def appeartwotimes(A, m):
    if not A:
        return 0
    index = 0
    comparer = 0
    for i in range(1, len(A)):
        it = A[i]
        if A[i] == A[index]:
            comparer += 1
            # don't move index
        if comparer - index + 1 == m and A[i] != A[index]:
            A[comparer] = A[i]
            index = comparer
        if A[i] != A[index]:
            index += 1
            comparer += 1
        if i - index + 1 == m and i == len(A)-1:
            for i in range(m - 2):
                A.remove(it)
    return index

print(appeartwotimes(G, m))
print(G)

