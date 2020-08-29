### Find kth largest element in a not sorted array using heapify of heapq
###
import heapq


def find_Kth_largest(nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


print(find_Kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))