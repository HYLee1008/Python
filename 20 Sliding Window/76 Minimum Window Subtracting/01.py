### Find the minimum window that contains every elements of T using brute force
### O(n^2)
def min_window(s, t):
    def contains(s_substr_lst, t_lst):
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True

    if not s or not t:
        return ''

    window_size = len(t)

    for size in range(window_size, len(s) + 1):
        for left in range(len(s) - size + 1):
            s_substr = s[left:left + size]
            if contains(list(s_substr), list(t)):
                return s_substr
    return ''


print(min_window('ADOBECODEBANC', 'ABC'))