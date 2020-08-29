### Find kth largest element in a not sorted array using heapq module
###
import heapq


def find_Kth_largest(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


print(find_Kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))