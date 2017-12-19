def day16_1(initial_line, filename):
    line = list(initial_line)
    dance = readfile(filename)
    for move in dance:
        line = perform_move(line, move)
    return ''.join(line)

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

SPIN = 's'
EXCHANGE = 'x'
PARTNER = 'p'

def readfile(filename):
    with open(filename) as file:
        return file.readline().split(',')
