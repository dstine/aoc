DIM = 300

def part1(serial_number):
    power = {}
    for y in range(1, DIM+1):
        for x in range(1, DIM+1):
            power[(x, y)] = calc_power((x, y), serial_number)
    max_power = 0
    max_coords =(0, 0)
    for y in range(2, DIM):
        for x in range(2, DIM):
            val = 0
            for iy in range(-1, 2):
                for ix in range(-1, 2):
                    val += power[(x+ix, y+iy)]
            if val > max_power:
                max_power = val
                max_coords = (x-1, y-1)
    return max_coords

def calc_power(coord, serial_number):
    rack_id = coord[0] + 10
    level = rack_id * coord[1]
    level += serial_number
    level *= rack_id
    level %= 1000
    level //= 100
    level -= 5
    return level
