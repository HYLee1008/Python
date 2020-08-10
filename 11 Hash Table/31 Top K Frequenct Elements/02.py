### Extract top K frequent element by pythonic way.
###
import collections

def top_k_frequent(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


input = [1, 1, 1, 2, 2, 3]
k = 2

print(top_k_frequent(input, k))