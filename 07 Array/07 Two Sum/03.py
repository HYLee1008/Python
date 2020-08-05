### Return the index that could make the target by summation without searching
### Best case: O(1), Worst case: O(n)
def two_sum(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))