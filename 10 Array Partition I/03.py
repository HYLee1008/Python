### Calculate the largest number that can be made from the sum of min(a, b) using n pairs by pythonic way.
### Fastest method by slicing.
def array_pair_sum(nums):
    return sum(sorted(nums)[::2])


input = [1, 4, 3, 2]
print(array_pair_sum(input))