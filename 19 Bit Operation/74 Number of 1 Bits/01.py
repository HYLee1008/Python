### Calculate nuber of 1 bits of given unsigned integer using count
###
def hamming_weight(n):
    return bin(n).count('1')