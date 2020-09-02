### Calculate the hamming distance between two given integer number using XOR
###
def hamming_distance(x, y):
    return bin(x ^ y).count('1')