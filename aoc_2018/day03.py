def part1(raw_claims):
    fabric = create_fabric(1000, 1000)
    return process_claims(fabric, raw_claims)

def part2(raw_claims):
    fabric = create_fabric(1000, 1000)
    process_claims(fabric, raw_claims)
    return find_intact_claim(fabric, raw_claims)

def process_claims(fabric, raw_claims):
    claims = [parse_claim(raw_claim) for raw_claim in raw_claims]
    for claim in claims:
        assert_claim(fabric, claim)
    count = 0
    for i in range(len(fabric)):
        for j in range(len(fabric)):
            if fabric[j][i] > 1:
                count += 1
    return count

def find_intact_claim(fabric, raw_claims):
    claims = [parse_claim(raw_claim) for raw_claim in raw_claims]
    for id, x, y, x_len, y_len in claims:
        intact = True
        for i in range(x, x + x_len):
            for j in range(y, y + y_len):
                if intact and fabric[j][i] > 1:
                    intact = False
                    break
        if intact:
            return id

def create_fabric(x_max, y_max):
    fabric = []
    for i in range(x_max):
        fabric.append([])
        fabric[i] = [0] * y_max
    return fabric

def parse_claim(raw_claim):
    pieces = raw_claim.split(' ')
    id = int(pieces[0][1:])
    # skip pieces[1], the '@' symbol
    # skip trailing ':' symbol
    x, y = pieces[2][:-1].split(',')
    x_len, y_len = pieces[3].split('x')
    return id, int(x), int(y), int(x_len), int(y_len)

def assert_claim(fabric, claim):
    _, x, y, x_len, y_len = claim
    for i in range(x, x + x_len):
        for j in range(y, y + y_len):
            fabric[j][i] += 1
