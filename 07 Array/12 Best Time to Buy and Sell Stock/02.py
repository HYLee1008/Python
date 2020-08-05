### Get the maximum profit of single transaction using kadane's algorithm
### O(n)
import sys

def max_profit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


input = [7, 1, 5, 3, 6, 4]
print(max_profit(input))