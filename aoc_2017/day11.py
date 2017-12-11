# Reference for hexagonal grid system including distance formula:
# http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/

ORIGIN = (1, 1, -2)
DIMENSIONS = 3

def day11_1(input):
    return day11(input)[0]

def day11_2(input):
    return day11(input)[1]

def day11(input):
    directions = input.split(',')
    location = list(ORIGIN)
    max_distance = 0
    for direction in directions:
        move(location, direction)
        distance = calc_distance(location)
        max_distance = max(distance, max_distance)
    final_distance = calc_distance(location)
    return (final_distance, max_distance)

MOVE_DELTAS = {
    'n':  ( 0,  1, -1),
    'ne': ( 1,  0, -1),
    'se': ( 1, -1,  0),
    's':  ( 0, -1,  1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0),
}

def move(location, direction):
    move_deltas = MOVE_DELTAS[direction]
    for n in range(DIMENSIONS):
        location[n] += move_deltas[n]

def calc_distance(location):
    axes = [abs(location[n] - ORIGIN[n]) for n in range(DIMENSIONS)]
    return max(axes)
