GRID_SIZE = 300

def part1(serial_number):
    powers = calc_powers(serial_number)
    _, max_coords = calc_max(powers, serial_number, 3)
    return max_coords

def part2(serial_number):
    powers = calc_powers(serial_number)
    max_power = 0
    max_coords = (0, 0)
    max_square_size = 0
    for square_size in range(1, GRID_SIZE+1):
        #print(square_size)
        power, coords = calc_max(powers, serial_number, square_size)
        if power > max_power:
            max_power = power
            max_coords = coords
            max_square_size = square_size
            #print(max_power, max_coords, max_square_size)
    return max_coords, max_square_size

def calc_max(powers, serial_number, square_size):
    max_dim = GRID_SIZE - square_size + 2
    max_power = 0
    max_coords = (0, 0)
    for y in range(1, max_dim):
        for x in range(1, max_dim):
            val = 0
            for dy in range(0, square_size):
                for dx in range(0, square_size):
                    val += powers[(x+dx, y+dy)]
            if val > max_power:
                max_power = val
                max_coords = (x, y)
    return max_power, max_coords

def calc_powers(serial_number):
    powers = {}
    for y in range(1, GRID_SIZE+1):
        for x in range(1, GRID_SIZE+1):
            powers[(x, y)] = calc_power((x, y), serial_number)
    return powers

def calc_power(coord, serial_number):
    rack_id = coord[0] + 10
    level = rack_id * coord[1]
    level += serial_number
    level *= rack_id
    level %= 1000
    level //= 100
    level -= 5
    return level
