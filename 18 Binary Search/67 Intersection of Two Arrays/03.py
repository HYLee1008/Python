### Find the interseciton of two arrays using two pointer
### O(nlogn)
def intersection(nums1, nums2):
    result = set()

    nums1.sort()
    nums2.sort()
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return result


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))