### Return permutations using itertools
###
import itertools

def permute(nums):
    return list(itertools.permutations(nums))


input = [1, 2, 3]
print(permute(input))