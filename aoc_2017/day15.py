def day15_1(a_start, b_start, num_pairs):
    return day15(a_start, 1, b_start, 1, num_pairs)

def day15_2(a_start, b_start, num_pairs):
    return day15(a_start, 4, b_start, 8, num_pairs)

A_FACTOR = 16807
B_FACTOR = 48271
DIVISOR = 2147483647

def day15(a_start, a_multiple_of, b_start, b_multiple_of, num_pairs):
    iterations = 0
    matches = 0
    a = a_start
    b = b_start
    while iterations < num_pairs:
        a = generate_next(a, A_FACTOR, a_multiple_of)
        b = generate_next(b, B_FACTOR, b_multiple_of)
        a_lo16 = a & 0xffff
        b_lo16 = b & 0xffff
        a_lo16 = bin(a_lo16)
        b_lo16 = bin(b_lo16)
        if a_lo16 == b_lo16:
            matches += 1
        iterations += 1
    return matches

def generate_next(current, factor, multiple_of):
    candidate = current
    while True:
        candidate = candidate * factor % DIVISOR
        if candidate % multiple_of == 0:
            return candidate
