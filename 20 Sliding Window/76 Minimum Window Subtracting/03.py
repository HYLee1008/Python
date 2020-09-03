### Find the minimum window that contains every elements of T using counter
### O(n)
import collections


def min_window(s, t):
    t_count = collections.Counter(t)
    current_count = collections.Counter()

    start = float('-inf')
    end = float('inf')

    left = 0
    for right, char in enumerate(s, 1):
        current_count[char] += 1
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1

    return s[start: end] if end - start <= len(s) else ''


print(min_window('ADOBECODEBANC', 'ABC'))