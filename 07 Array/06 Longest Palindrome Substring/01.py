### Printing longest palindrome substring by two pointer
def longest_palindrome(s):
    # determine palindrome and expand two pointer
    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1: right - 1]

    # exception
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # move sliding window to right side
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


input_1 = 'babad'
input_2 = 'cbbd'

print(longest_palindrome(input_1))
print(longest_palindrome(input_2))