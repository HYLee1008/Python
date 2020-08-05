### Remove duplicate letters and maek it lexicographical order by stack.
###
from collections import Counter

def remove_duplicate_letters(s):
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


input_1 = "bcabc"
input_2 = "cbacdcbc"

print(remove_duplicate_letters(input_1))
print(remove_duplicate_letters(input_2))