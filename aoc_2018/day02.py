def count(id):
    counts = {}
    for c in id:
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1
    has_double = False
    has_triple = False
    for c, count in counts.items():
        if count == 2:
            has_double = True
        elif count == 3:
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
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            matches += id1[i]
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
