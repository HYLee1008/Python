### Calculate nuber of 1 bits of given unsigned integer using bit operation.
###
def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count