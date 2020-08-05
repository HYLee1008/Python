### Valid palindrome using deque
### popleft function of deque is O(1). Much efficient than list
import time
import collections

def is_palindrome(s: str) -> bool:
    # declare deque
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

input_1 = "A man, a plan, a canal: Panama"
input_2 = "race a car"

start_time = time.time()
print(is_palindrome(input_1))
print(is_palindrome(input_2))
print(f'Time taken: {time.time() - start_time}')