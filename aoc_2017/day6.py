import functools

def day6_1(memory):
    cycles_until_repeat = 0
    seen = []
    while True:
        cycles_until_repeat += 1
        selected_entry = select_entry(memory)
        allocate_entry(memory, selected_entry)
        t = tuple(memory)
        if t in seen:
            return cycles_until_repeat
        else:
            seen.append(t)

def select_entry(memory):
    indexed_memory = list(enumerate(memory)) # zipWithIndex
    selected_entry = functools.reduce(
        lambda result, incoming: incoming if incoming[1] > result[1] else result,
        indexed_memory, (0, 0))
    return selected_entry

def allocate_entry(memory, entry):
    idx = entry[0]
    value = entry[1]
    memory[idx] = 0
    while (value > 0):
        idx += 1
        if idx == len(memory):
            idx = 0
        memory[idx] += 1
        value -= 1
