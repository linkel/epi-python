# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D
# and updates the array to represent the integer D+1.
# i.e., if the input is [1, 2, 9] then the array should become [1, 3, 0].

A = [1, 2, 9]

# the following is a brute force solution where I turn the array into an int and increment it then convert it back

def increment(A):
    res = []
    joined = ''
    for item in A:
        joined = joined + str(item)
    print(joined)
    incremented = int(joined) + 1
    for char in str(incremented):
        res.append(int(char))
    return res

print(increment(A))

# the above, if a limit on the range of integer values exists (like in another language),
# will fail on inputs outside of that range

# to avoid these overflow issues, we can operate directly on the array
# we can add digits at the end and propagate the "carries" to the next

def grade_school(A):
    # add one to the end of the array
    A[-1] += 1
    # from the last thing in the array to the second thing
    for i in reversed(range(1, len(A))):
        # we want to not do this loop if nothing's a ten starting from the ones place
        if A[i] != 10:
            break
        # if something is a ten, now we continue
        # that last digit gets set to zero and the next one gets a 1 added
        # if that made it a 10 then we're going to it next anyway, and if it didn't we'll break out
        A[i] = 0
        A[i - 1] += 1
    # if the very first element is a 10 though we have to make a new place for it at the beginning
    # and append a zero to the end, since for example 999 would become 1000
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

# for example, it'd go from [9, 9] to [9, 10] to [10, 0] to [1, 0, 0]. 

# The time complexity is O(n) where n is the length of A. 

# Write a program which takes as input two strings "s" and "t" of bits encoding binary numbers Bs and Bt
# and returns a new string of bits representing the number Bs + Bt

s = "100"
t = "101"

def bitstring(s, t):
    intRes = int(s, 2) + int(t, 2)
    res = str(bin(intRes))
    return res[2:]
    
print(bitstring(s, t))

# Kind of feel like using python's built-in functions here is a bit cheating. 