# Write a program that takes an array A of n numbers and rearranges A's
# elements to get a new array B that has the property B[0] <= B[1] >= B[2] <= B[3]...

A = [1, 2, 3, 4, 5, 6]
B = [3, 3, 2, 6, 6, 1, 4, 6, 2, 3, 3, 3]
# If we sort the array and interleave the bottom and top halves, we get a O(n log n) time solution.

# Could also arrange elements around the median and then interleave. That would be O(n).

# However since the ordering is very local, you don't have to find median. 

def rearrange(A):
    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)

rearrange(A)
print(A)
rearrange(B)
print(B)