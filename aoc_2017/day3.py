# observe that for each "ring" of the grid, we take the same number of steps
# for each of the four directions
#   allocate  9 -  1 =  8 = 2 in each of 4 directions
#   allocate 25 -  9 = 16 = 4 in each of 4 directions
#   allocate 49 - 25 = 24 = 6 in each of 4 directions
def day3_1(num):
    location = [0,0]
    value = 1
    grid = {}

    update(grid, value, location)
    value += 1

    steps_per_dir = 0
    while value <= num:
        steps_per_dir += 2
        step_right(location)
        step_down(location)
        value = fill_edge(grid, value, location, steps_per_dir, step_up)
        value = fill_edge(grid, value, location, steps_per_dir, step_left)
        value = fill_edge(grid, value, location, steps_per_dir, step_down)
        value = fill_edge(grid, value, location, steps_per_dir, step_right)
    return abs(grid[num][0]) + abs(grid[num][1])

def fill_edge(grid, value, location, steps_per_dir, take_step):
    for i in range(steps_per_dir):
        take_step(location)
        update(grid, value, location)
        value += 1
    return value

def step_right(location):
    location[0] += 1

def step_up(location):
    location[1] += 1

def step_left(location):
    location[0] -= 1

def step_down(location):
    location[1] -= 1

def update(grid, value, location):
    grid[value] = tuple(location)
