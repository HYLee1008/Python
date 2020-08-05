### Valid palindrome using list
### pop(0) of list is O(n), which is inefficient.
import time

def is_palindrome(s: str) -> bool:
    # get character only
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # determine whether it is palindrome or not
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

input_1 = "A man, a plan, a canal: Panama"
input_2 = "race a car"

start_time = time.time()
print(is_palindrome(input_1))
print(is_palindrome(input_2))
print(f'Time taken: {time.time() - start_time}')