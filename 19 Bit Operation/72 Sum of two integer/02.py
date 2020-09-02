### Calculate sum of two integer without + or - operator.
### Implementing full adder. Much simpler version
def get_sum(a, b):
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a > INT_MAX:
        a = ~(a ^ MASK)
    return a