A_FACTOR = 16807
B_FACTOR = 48271
DIVISOR = 2147483647
MASK = 2 ** 16

def day15_1(a_start, b_start, num_pairs):
    iterations = 0
    matches = 0
    a = a_start
    b = b_start
    while iterations < num_pairs:
        a = a * A_FACTOR % DIVISOR
        b = b * B_FACTOR % DIVISOR
        a_lo16 = bin(a % MASK)
        b_lo16 = bin(b % MASK)
        if a_lo16 == b_lo16:
            matches += 1
        iterations += 1
    return matches
