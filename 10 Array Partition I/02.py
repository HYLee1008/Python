### Calculate the largest number that can be made from the sum of min(a, b) using n pairs by even index number.
###
def array_pair_sum(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


input = [1, 4, 3, 2]
print(array_pair_sum(input))