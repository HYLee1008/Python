### Convert sorted array to binary search tree using binary search
###
from datastructure import TreeNode


def sorted_array_to_list(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sorted_array_to_list(nums[:mid])
    node.right = sorted_array_to_list(nums[mid + 1:])

    return node