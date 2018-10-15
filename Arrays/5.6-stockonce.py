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

