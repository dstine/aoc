# observe that for each "ring" of the grid, we take the same number of steps
# for each of the four directions
#   allocate  9 -  1 =  8 = 2 in each of 4 directions
#   allocate 25 -  9 = 16 = 4 in each of 4 directions
#   allocate 49 - 25 = 24 = 6 in each of 4 directions
def day3_1(num):
    curr_location = [0,0]
    value_holder = [1]
    grid = {}

    fill_value(grid, value_holder[0], curr_location)
    value_holder[0] += 1

    steps_per_dir = 0
    while value_holder[0] <= num:
        steps_per_dir += 2
        step_right(curr_location)
        step_down(curr_location)
        fill_edge_1(grid, value_holder, curr_location, steps_per_dir, step_up)
        fill_edge_1(grid, value_holder, curr_location, steps_per_dir, step_left)
        fill_edge_1(grid, value_holder, curr_location, steps_per_dir, step_down)
        fill_edge_1(grid, value_holder, curr_location, steps_per_dir, step_right)

    for loc, val in grid.items():
        if val == num:
            return abs(loc[0]) + abs(loc[1])

def fill_edge_1(grid, value_holder, curr_location, steps_per_dir, take_step):
    for i in range(steps_per_dir):
        take_step(curr_location)
        fill_value(grid, value_holder[0], curr_location)
        value_holder[0] += 1

def day3_2(num):
    curr_location = [0,0]
    grid = {}

    fill_value(grid, 1, curr_location)

    steps_per_dir = 0
    while True:
        steps_per_dir += 2
        step_right(curr_location)
        step_down(curr_location)
        ret = 0
        ret = fill_edge_2(grid, num, curr_location, steps_per_dir, step_up)
        if ret != 0:
            return ret
        ret = fill_edge_2(grid, num, curr_location, steps_per_dir, step_left)
        if ret != 0:
            return ret
        ret = fill_edge_2(grid, num, curr_location, steps_per_dir, step_down)
        if ret != 0:
            return ret
        ret = fill_edge_2(grid, num, curr_location, steps_per_dir, step_right)
        if ret != 0:
            return ret

def fill_edge_2(grid, num, curr_location, steps_per_dir, take_step):
    for i in range(steps_per_dir):
        take_step(curr_location)
        value = calc_value(grid, curr_location)
        if value > num:
            return value
        fill_value(grid, value, curr_location)
    return 0

def calc_value(grid, curr_location):
    sum = 0
    sum += grid.get((curr_location[0]+1, curr_location[1]  ), 0)
    sum += grid.get((curr_location[0]+1, curr_location[1]+1), 0)
    sum += grid.get((curr_location[0],   curr_location[1]+1), 0)
    sum += grid.get((curr_location[0]-1, curr_location[1]+1), 0)
    sum += grid.get((curr_location[0]-1, curr_location[1]  ), 0)
    sum += grid.get((curr_location[0]-1, curr_location[1]-1), 0)
    sum += grid.get((curr_location[0],   curr_location[1]-1), 0)
    sum += grid.get((curr_location[0]+1, curr_location[1]-1), 0)
    return sum

### common to both parts

def step_right(curr_location):
    curr_location[0] += 1

def step_up(curr_location):
    curr_location[1] += 1

def step_left(curr_location):
    curr_location[0] -= 1

def step_down(curr_location):
    curr_location[1] -= 1

def fill_value(grid, value, curr_location):
    grid[tuple(curr_location)] = value
