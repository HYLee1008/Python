### Return longest substring without repeating characters by sliding window and two pointer
###
def length_of_longest_substring(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index

    return max_length


input_1 = "abcabcbb"
input_2 = "bbbbb"
input_3 = "pwwkew"

print(length_of_longest_substring(input_1))
print(length_of_longest_substring(input_2))
print(length_of_longest_substring(input_3))