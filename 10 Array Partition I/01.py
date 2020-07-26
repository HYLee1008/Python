### Calculate the largest number that can be made from the sum of min(a, b) using n pairs by ascending order.
###
def array_pair_sum(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


input = [1, 4, 3, 2]
print(array_pair_sum(input))