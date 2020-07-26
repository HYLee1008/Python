### Get the product of array except itsetl.
### O(n)
def product_except_self(nums):
    out = []
    p = 1
    # product left side
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # product right side on result of left side
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out


input = [1, 2, 3, 4]
print(product_except_self(input))