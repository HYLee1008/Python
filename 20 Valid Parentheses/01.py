### Determine valid parentheses using stack
### Every stack operation using lisg is O(1)
def is_valid(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


input = '()[]{}'
print(is_valid(input))