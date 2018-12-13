def part1(initial_state, rules, n_generations):
    #print()
    state = {}
    for i in range(len(initial_state)):
        state[i] = initial_state[i]
    #print('{:2d}: {}'.format(0, state_as_string(state)))
    for gen in range(1, n_generations+1):
        state = generation(state, rules)
        #print('{:2d}: {}'.format(gen, state_as_string(state)))
        # use this to find pattern to build formulas for part2
        #print('{:2d}: {}'.format(gen, calc_result(state)))
    return calc_result(state)

def part2_example(initial_state, rules, n_generations):
    if n_generations < 100:
        return part1(initial_state, rules, n_generations)
    else:
        return ((n_generations - 86) * 20) + 1094

def part2_input(initial_state, rules, n_generations):
    if n_generations < 120:
        return part1(initial_state, rules, n_generations)
    else:
        return ((n_generations - 120) * 46) + 5526

def generation(state, rules):
    next_state = state.copy()
    for num in range(min(state.keys()), max(state.keys())+1):
        window = []
        for n in range(-2, 3):
            idx = num + n
            if idx not in state:
                state[idx] = '.'
                next_state[idx] = '.'
            window.append(state[idx])
        window = ''.join(window)
        next_val = rules[window] if window in rules else '.'
        #print('    {:2d} {}   {}'.format(num, pots, next_val))
        next_state[num] = next_val
    return next_state

def state_as_string(state):
    val = []
    for i in range(min(state.keys()), max(state.keys())+1):
        val.append(state[i])
    return ''.join(val)

def calc_result(state):
    return sum([num for num, pot in state.items() if pot == '#'])
