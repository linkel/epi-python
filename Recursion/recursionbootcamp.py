def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

print(gcd(160, 30))

# time complexity is O(n) where n is the bits needed to represent inputs. 
# or O(log max(x,y)) since an argument is at least halved each time
# space is O(n) due to depth of the function call stack. 
# could convert it to a loop which would use O(1)

# recursion good for search, enumeration, and divide and conquer
# use recursion as an alternative to deeply nested loops

# if asked to remove recursion. can copy call stack with a stack
# recursion can be removed from a tail-recursive problem by using a while

# if a recursive fn can be called with the same arguments more than once,
# cache the results (turns into dynamic programming)

