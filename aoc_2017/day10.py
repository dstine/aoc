from  functools import reduce

def day10_1(lst_length, lengths_input):
    return day10(lst_length, lengths_input, calc_lengths_1, 1, product_first_two)

def day10_2(lst_length, lengths_input):
    return day10(lst_length, lengths_input, calc_lengths_2, 64, hash_in_hex)

def day10(lst_length, lengths_input, calc_lengths, rounds, calc_result):
    lst = [n for n in range(0, lst_length)]
    lengths = calc_lengths(lengths_input)
    skip_size = 0
    curr_pos = 0
    for _ in range(rounds):
        for length in lengths:
            indexes = calc_indexes(curr_pos, lst, length)
            reverse(indexes, lst)
            curr_pos += length + skip_size
            curr_pos %= len(lst)
            skip_size += 1
    return calc_result(lst)

def calc_indexes(curr_pos, lst, length):
    indexes = list(range(curr_pos, curr_pos + length))
    indexes = [i if i < len(lst) else i - len(lst) for i in indexes]
    return indexes

def reverse(indexes, lst):
    while len(indexes) not in [0, 1]:
        first_idx, last_idx = indexes[0], indexes[-1]
        indexes.pop(0)
        indexes.pop(-1)
        tmp = lst[first_idx]
        lst[first_idx] = lst[last_idx]
        lst[last_idx] = tmp

def product_first_two(lst):
    return lst[0] * lst[1]

NUM_BLOCKS = 16
BLOCK_SIZE = 16

def hash_in_hex(lst):
    dense_hash = [bitwise_xor(lst[BLOCK_SIZE*i : BLOCK_SIZE*i + BLOCK_SIZE]) for i in range(NUM_BLOCKS)]
    hex_hash = [hex(n).replace('0x', '') for n in dense_hash]
    hex_hash = [h if len(h) == 2 else '0' + h for h in hex_hash]
    return reduce(lambda a, b: a + b, hex_hash, '')

def bitwise_xor(sub_lst):
    return reduce(lambda a, b: a ^ b, sub_lst, 0)

def calc_lengths_1(lengths_input):
    return [int(n) for n in lengths_input.split(',')]

STANDARD_LENGTH_SUFFIX = [17, 31, 73, 47, 23]

def calc_lengths_2(lengths_input):
    lengths = as_ascii(lengths_input)
    return lengths + STANDARD_LENGTH_SUFFIX

def as_ascii(lengths_input):
    return [ord(char) for char in lengths_input]
