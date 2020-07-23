### Reversing string using pythonic way
import time

def reverse_string(s) -> None:
    s.reverse()
    # s[:] = s[::-1]


input_1 = ['h', 'e', 'l', 'l', 'o']
input_2 = ['H', 'a', 'n', 'n', 'a', 'h']

reverse_string(input_1)
reverse_string(input_2)

print(input_1)
print(input_2)