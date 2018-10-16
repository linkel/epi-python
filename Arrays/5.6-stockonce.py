# buy and sell a stock once to make max profit over a day
# Take an array denoting daily stock price and return max profit that can be made by 
# buying and selling one share. no buy if no profit possible.

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

def profit(A):
    index = 0
    profits = []
    currProfit = 0
    for i in range(1, len(A)):
        if A[i] - A[index] > currProfit:
            currProfit = A[i] - A[index]
        elif A[i] - A[index] < 0 and currProfit != 0:
            profits.append(currProfit)
            index = i
            currProfit = 0
    profits.append(currProfit) # to get the last one
    return max(profits)

print(profit(A))

# My answer is O(n) time and O(n) space due to the list.

# The book's example, which doesn't need another list to store any more info.
# time complexity O(n) and space O(1)

def stockonce(A):
    minPrice, maxProfit = float('inf'), 0.0
    for price in A:
        maxProfitToday = price - minPrice
        maxProfit = max(maxProfit, maxProfitToday)
        minPrice = min(minPrice, price)
    return maxProfit

# Write a program that takes an array of integers and finds the length of a longest subarray all of whose entries are equal.

B = [2, 4, 6, 9, 9, 9, 3, 6, 2, 1, 5, 5, 5, 5, 2]
C = []

def longest(A):
    consecutiveCount, current, longest = 1, None, 0
    if len(A) == 0:
        return 0
    for i in A:
        if current != i:
            current = i
            consecutiveCount = 1
        elif current == i:
            consecutiveCount += 1
            longest = max(longest, consecutiveCount)
    return longest

print(longest(B))

# I think the above works. I really like the way the book uses max() to keep saving the best one.
# I've tended to use awkward list constructions or two variables that get compared to each other.
# It's probably good to know multiple methods though since other languages won't have a max(). 

# The above is O(n) time and O(1) space.