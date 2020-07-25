### Return the index that could make the target by summation using searching by in.
### O(n^2). Same time complexity with brute-force but more efficient.
def two_sum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i + 1)


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))