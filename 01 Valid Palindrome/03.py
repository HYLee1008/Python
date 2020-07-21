### Valid palindrome using slicing
### Slicing is realized based on C, so it is much faster than ordinary python functions.
### Slicing is the fastest way whan using string structure. So, it is recomended to use slicing as a priory.
import time
import re

def is_palindrome(s: str) -> bool:
    s = s.lower()
    # filter string using re.sub
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # Slicing

input_1 = "A man, a plan, a canal: Panama"
input_2 = "race a car"

start_time = time.time()
print(is_palindrome(input_1))
print(is_palindrome(input_2))
print(f'Time taken: {time.time() - start_time}')