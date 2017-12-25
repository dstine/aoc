def day5_1(instructions):
    return day5(instructions, offset_by_one)

def day5_2(instructions):
    return day5(instructions, offset_strange)

def offset_by_one(offset):
    return 1

def offset_strange(offset):
    return -1 if offset >= 3 else 1

def day5(instructions, offset_rule):
    ptr = 0
    jumps = 0
    while True:
        offset = instructions[ptr]
        new_ptr = ptr + offset
        jumps += 1
        if 0 <= new_ptr < len(instructions):
            instructions[ptr] += offset_rule(offset)
            ptr = new_ptr
        else:
            return jumps
