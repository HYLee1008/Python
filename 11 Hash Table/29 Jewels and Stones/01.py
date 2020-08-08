### calculate how many jewels in stones using hash table.
###
def num_jewels_in_stones(J, S):
    freqs = {}
    count = 0

    # calculate frequency of stone(S)
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # Sum frequency of jewels(J)
    for char in J:
        if char in freqs:
            count += freqs[char]

    return count


J = "aA"
S = "aAAbbbb"

print(num_jewels_in_stones(J, S))