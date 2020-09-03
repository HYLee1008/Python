### Find the maximum profit using pythonic method
###
def max_profit(prices):
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


print(max_profit([7, 1, 5, 3, 6, 4]))