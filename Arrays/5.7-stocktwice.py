# Write a program that computes the max profit that can be made by buying and selling a share at most twice.
# Second buy must be made on another date after the first sale. 

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
B = [12,11,13,9,12,8,14,13,15]
# hijacking my answer from the last one...

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
    best = max(profits)
    profits.remove(best)
    return best + max(profits)

print(profit(B))

# So I was lazy and just removed the max from the list and called max() again. 
# It's O(n) time and O(n) space again.

# Book says that brute force solution examining all combos of buy sell buy sell is complexity O(n^4). 
# Book says you can bring complexity down to O(n^2) by applying the O(n) algo to each pair of subarrays.
# So recording the previous computation is a good idea.

# book solution follows. Time complexity O(n) and space O(n) because of storing the best solutions.

def buy_and_sell_stock_twice(prices):

    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that
    # day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we make the
    # second buy on that day.
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i - 1])
    return max_total_profit

# Solve the same problem in O(n) time and O(1) space.

