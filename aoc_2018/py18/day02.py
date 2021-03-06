def count(id):
    has_double = False
    has_triple = False
    for c in id:
        if not has_double and id.count(c) == 2:
            has_double = True
        elif not has_triple and id.count(c) == 3:
            has_triple = True
    return (has_double, has_triple)

def part1(ids):
    doubles = 0
    triples = 0
    for id in ids:
        has_double, has_triple = count(id)
        if has_double:
            doubles += 1
        if has_triple:
            triples += 1
    return doubles * triples

def compare(id1, id2):
    num_diffs = 0
    matches = ''
    for pair in zip(id1, id2):
        if pair[0] == pair[1]:
            matches += pair[0]
        else:
            num_diffs += 1
    return (num_diffs, matches)

import sys
def part2(ids):
    best = (sys.maxsize, '')
    for i, id1 in enumerate(ids):
        for id2 in ids[i+1:]:
            result = compare(id1, id2)
            if result[0] < best[0]:
                best = result
    return best[1]
