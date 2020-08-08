### Calculate how many jewels in stones. Remove comparison using defaultdict.
###
import collections

def num_jewels_in_stones(J, S):
    freqs = collections.defaultdict(int)
    count = 0

    # calculate frequency of stone(S)
    for char in S:
        freqs[char] += 1

    # Sum frequency of jewels(J)
    for char in J:
        count += freqs[char]

    return count


J = "aA"
S = "aAAbbbb"

print(num_jewels_in_stones(J, S))