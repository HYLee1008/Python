### Find kth largest element in a not sorted array using nlargest of heapq
###
import heapq


def find_Kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


print(find_Kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))