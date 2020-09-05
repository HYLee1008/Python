### Find majority element using brute force
###
def majority_element(nums):
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num


print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))