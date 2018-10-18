import math
# Enumerate all primes between 1 and an integer input argument. 

A = 18
def primebrute(x):
    primeList = []
    checker = True
    for i in range(2, x):
        for j in range(2,math.floor(math.sqrt(i))+1):
            if i % j !=0:
                checker = True
            elif i % j == 0:
                checker = False
                break
        if checker == True:
            primeList.append(i)
        else:
            checker = True
    return primeList
    
print(primebrute(A))

# The above brute force solution is O(n^3/2) time complexity.

# book gives an example of a sieving approach:

def generate_primes(n):
    primes = []
    isPrime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if isPrime[p]:
            primes.append(p)
            for i in range(p, n+1, p):
                isPrime[i] = False
    return primes

print(generate_primes(18))

# yields O(n log log n) time because the time it takes to sift is proportional to n/p
# but the storage is O(n).