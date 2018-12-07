import sys
from collections import defaultdict

def part1(coords):
    x_lo = min([coord[0] for coord in coords])
    x_hi = max([coord[0] for coord in coords])
    y_lo = min([coord[1] for coord in coords])
    y_hi = max([coord[1] for coord in coords])
    grid = defaultdict(lambda: -1)
    for x in range(x_lo, x_hi + 1):
        for y in range(y_lo, y_hi + 1):
            grid[(x, y)] = label_nearest((x, y), coords)

    edge_labels = set()
    for x in range(x_lo, x_hi + 1):
        edge_labels.add(grid[(x, y_lo)])
        edge_labels.add(grid[(x, y_hi)])
    for y in range(y_lo, y_hi + 1):
        edge_labels.add(grid[(x_lo, y)])
        edge_labels.add(grid[(x_hi, y)])

    all_labels = set(range(len(coords)))
    interior_labels = all_labels - edge_labels
    counts = defaultdict(int)
    for x in range(x_lo, x_hi + 1):
        for y in range(y_lo, y_hi + 1):
            label = grid[(x, y)]
            if label in interior_labels:
                counts[label] += 1
    return max(counts.values())

def label_nearest(cell, coords):
    closest_distance = sys.maxsize
    closest_indexes = [-1]
    for i, coord in enumerate(coords):
        dist = distance(cell, coord)
        if dist < closest_distance:
            closest_distance = dist
            closest_index = [i]
        elif dist == closest_distance:
            closest_index.append(i)
    if len(closest_index) > 1:
        return -1
    else:
        return closest_index[0]

def part2(coords, threshold):
    x_lo = min([coord[0] for coord in coords])
    x_hi = max([coord[0] for coord in coords])
    y_lo = min([coord[1] for coord in coords])
    y_hi = max([coord[1] for coord in coords])
    grid = defaultdict(lambda: -1)
    for x in range(x_lo, x_hi + 1):
        for y in range(y_lo, y_hi + 1):
            grid[(x, y)] = label_total_distance((x, y), coords)
    return sum([1 if v < threshold else 0 for v in grid.values()])

def label_total_distance(cell, coords):
    return sum([distance(cell, coord) for coord in coords])

def distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
