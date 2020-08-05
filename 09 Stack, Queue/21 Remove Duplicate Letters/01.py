### Remove duplicate letters and maek it lexicographical order by recursive
###
def remove_duplicate_letters(s):
    # sort using set
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + remove_duplicate_letters(suffix.replace(char, ''))
    return ''


input_1 = "bcabc"
input_2 = "cbacdcbc"

print(remove_duplicate_letters(input_1))
print(remove_duplicate_letters(input_2))