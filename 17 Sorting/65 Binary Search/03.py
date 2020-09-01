### Find the index of the target using binary search by binary search module
###
import bisect


def search(nums, target):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1


print(search([-1, 0, 3, 5, 9, 12], 9))