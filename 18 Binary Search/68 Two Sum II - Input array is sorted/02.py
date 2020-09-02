### Find the index of the array that can make the target number by summation using two pointer
### O(nlogn)
def two_sum(numbers, target):
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        expected = target - v

        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] > expected:
                right = mid - 1
            elif numbers[mid] < expected:
                left = mid + 1
            else:
                return k + 1, mid + 1
