### Find the maximum sliding winodw
### Ineffective brute force method. O(n)
import collections


def max_sliding_window(nums, k):
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue


        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        if current_max == window.popleft():
            current_max = float('-inf')
    return results


print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))