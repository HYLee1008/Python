### Find the maximum profit using greedy algorithm
###
def max_profit(prices):
    result = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result


print(max_profit([7, 1, 5, 3, 6, 4]))