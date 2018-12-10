import re

def part1(input):
    points = parse(input)
    last_points = points
    last_area = calc_area(points)
    while True:
        points = step(points)
        area = calc_area(points)
        # assume that area decreases exactly until message appears
        if area < last_area:
            last_points = points
            last_area = area
        else:
            return format_sky(last_points)

def parse(input):
    points = []
    prog = re.compile('position=<([\-\d]*),([\-\d]*)>velocity=<([\-\d]*),([\-\d]*)>')
    for line in input:
        line = line.replace(' ', '')
        px, py, vx, vy = prog.match(line).groups()
        points.append([int(px), int(py), int(vx), int(vy)])
    return points

def calc_area(points):
    max_x, min_x, max_y, min_y = calc_bounds(points)
    return abs(max_x - min_x) * abs(max_y - min_y)

def format_sky(points):
    max_x, min_x, max_y, min_y = calc_bounds(points)
    coords = [(p[0], p[1]) for p in points]
    sky = ''
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in coords:
                sky += '#'
            else:
                sky += '.'
        sky += '\n'
    return sky

def calc_bounds(points):
    max_x = max([p[0] for p in points])
    min_x = min([p[0] for p in points])
    max_y = max([p[1] for p in points])
    min_y = min([p[1] for p in points])
    return max_x, min_x, max_y, min_y

def step(points):
    return [[p[0]+p[2], p[1]+p[3], p[2], p[3]] for p in points]
