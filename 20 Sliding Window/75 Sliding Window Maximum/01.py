### Find the maximum sliding winodw
### Ineffective brute force method. O(n)
def max_sliding_window(nums, k):
    if not nums:
        return nums

    r = []
    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i + k]))

    return r


print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))