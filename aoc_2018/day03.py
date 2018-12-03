def part1(claims):
    fabric = create_fabric(1000, 1000)
    for raw_claim in claims:
        claim = parse_claim(raw_claim)
        assert_claim(fabric, claim)
    count = 0
    for i in range(1000):
        for j in range(1000):
            if fabric[j][i] > 1:
                count += 1
    return count

def create_fabric(x_max, y_max):
    fabric = []
    for i in range(x_max):
        fabric.append([])
        fabric[i] = [0] * y_max
    return fabric

def parse_claim(claim):
    pieces = claim.split(' ')

    id = int(pieces[0][1:])

    # skip pieces[1], the '@' symbol

    coords = pieces[2].split(',')
    x = int(coords[0])
    # skip trailing ':' symbol
    y = int(coords[1][:-1])

    lengths = pieces[3].split('x')
    x_len = int(lengths[0])
    y_len = int(lengths[1])

    return (id, (x, y), (x_len, y_len))

def assert_claim(fabric, claim):
    coords = claim[1]
    x = coords[0]
    y = coords[1]
    lengths = claim[2]
    x_len = lengths[0]
    y_len = lengths[1]
    for i in range(x, x + x_len):
        for j in range(y, y + y_len):
            fabric[j][i] += 1
