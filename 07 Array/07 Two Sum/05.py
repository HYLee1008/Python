### Return the index that could make the target by summation using two pointer
### O(n), but it requires additional sorted data. We can use two pointer method only when data is sorted.
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # move right pointer when sum is larger than target
        if nums[left] + nums[right] < target:
            left += 1

        # move left pointer when sum is smaller than target
        elif nums[left] + nums[right] > target:
            right -= 1
        
        else:
            return left, right


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))