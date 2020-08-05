### Reversing string using two pointer
import time

def reverse_string(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

input_1 = ['h', 'e', 'l', 'l', 'o']
input_2 = ['H', 'a', 'n', 'n', 'a', 'h']

reverse_string(input_1)
reverse_string(input_2)

print(input_1)
print(input_2)