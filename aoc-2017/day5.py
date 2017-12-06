def day5_1(instructions):
    ptr = 0
    jumps = 0
    while True:
        offset = instructions[ptr]
        new_ptr = ptr + offset
        jumps += 1
        #print("{} {} {} {} {}".format(instructions, ptr, jumps, offset, new_ptr))
        if 0 <= new_ptr < len(instructions):
            instructions[ptr] += 1
            ptr = new_ptr
        else:
            return jumps