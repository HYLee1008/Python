### Return the index that could make the target by summation using brute force
### It is most easy and inefficient method. O(n^2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))