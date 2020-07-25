### Return the index that could make the target by summation by improving searching.
### Only 1 for loop, but has no big time advantage
def two_sum(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))