### Calculate how many jewels in stones. Remove calculation part using counter.
###
import collections

def num_jewels_in_stones(J, S):
    freqs = collections.Counter(S)
    count = 0

    # calculate the frequency of jewels(J)
    for char in J:
        count += freqs[char]

    return count


J = "aA"
S = "aAAbbbb"

print(num_jewels_in_stones(J, S))