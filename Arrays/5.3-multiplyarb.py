# Write a program that takes two arrays representing integers and returns
# an array of integers representing their product. 
# for example take 193707721 x -761838257287 = -147573952589676412927
# inputs are in array format and function will return [-1, 4, 7, 5, 7...] so on

A = [1,2,0]
B = [1,2,9]
C = [0, 0]

def multArb(A, B):
    # set the sign according to the first digit's sign
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    # make all ints we work with positive
    A[0], B[0] = abs(A[0]), abs(B[0])
    # make an array sized to be the length of A and B together since that's the max from multiplying
    res = [0] * (len(A) + len(B))
    # starting from the end of both
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            print(res)
            res[i + j + 1] += A[i] * B[j]
            print(res)
            res[i + j] += res[i + j + 1] // 10
            print(res)
            res[i + j + 1] %= 10
            print(res)
    # removes the leading zeroes or returns 0 if there's nothing to go through
    res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]
    return [sign * res[0]] + res[1:]

print(multArb(A, B))
