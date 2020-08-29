### Find kth largest element in a not sorted array using sorting
###
def find_Kth_largest(nums, k):
    return sorted(nums, reverse=True)[k - 1]


print(find_Kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))