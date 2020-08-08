### Calculate how many jewels in stones. Pythonic way.
###
def num_jewels_in_stones(J, S):
    return sum(s in J for s in S)


J = "aA"
S = "aAAbbbb"

print(num_jewels_in_stones(J, S))