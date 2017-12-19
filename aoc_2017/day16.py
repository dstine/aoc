def day16_1(initial_line, filename):
    return day16(initial_line, filename, 1)

def day16_2(initial_line, filename):
    # runtime is not acceptable; implement cycle detection
    #return day16(initial_line, filename, 1000000000)
    return 0

def day16(initial_line, filename, repeats):
    line = list(initial_line)
    moves = readfile(filename)
    seen = {}
    while repeats > 0:
        key = tuple(line)
        if key in seen:
            line = seen[key]
        else:
            for move in moves:
                line = perform_move(line, move)
            seen[key] = line
        repeats -= 1
    return ''.join(line)

SPIN = 's'
EXCHANGE = 'x'
PARTNER = 'p'

def perform_move(line, move):
    move_type = move[0]
    if SPIN == move_type:
        num = int(move[1:])
        return line[-num:] + line[:-num]
    elif EXCHANGE == move_type:
        separator = move.index('/')
        first = int(move[1:separator])
        second = int(move[separator+1:])
        tmp = line[first]
        line[first] = line[second]
        line[second] = tmp
        return line
    elif PARTNER == move_type:
        first = move[1]
        second = move[3]
        first_idx = line.index(first)
        second_idx = line.index(second)
        line[first_idx] = second
        line[second_idx] = first
        return line
    else:
        raise Exception('unknown move type')
    return ''

def readfile(filename):
    with open(filename) as file:
        return file.readline().split(',')
