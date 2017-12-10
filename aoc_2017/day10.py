def day10_1(lst_length, lengths_input):
    lst = [n for n in range(0, lst_length)]
    lengths = [int(n) for n in lengths_input.split(',')]
    skip_size = 0
    curr_pos = 0
    for length in lengths:
        indexes = calc_indexes(curr_pos, lst, length)
        reverse(indexes, lst)
        curr_pos += length + skip_size
        curr_pos %= len(lst)
        skip_size += 1
    return lst[0] * lst[1]

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
