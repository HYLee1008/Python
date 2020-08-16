### Return combinations using DFS
###
import itertools

def combine(n, k):
    return list(itertools.combinations(range(1, n + 1), k))


print(combine(4, 2))