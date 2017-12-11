from functools import reduce

def day6_1(memory):
    return day6(memory)[0]

def day6_2(memory):
    return day6(memory)[1]

def day6(memory):
    # key = tuple of memory bank configuration
    # value = list of cycles at which memory bank was seen
    seen = {}
    cycle = 0
    while True:
        cycle += 1
        selected_entry = select_entry(memory)
        allocate_entry(memory, selected_entry)
        key = tuple(memory)
        if key in seen:
            seen[key].append(cycle)
            # third encounter is the second repeat
            if len(seen[key]) == 3:
                second_encounter_cycles = seen[key][-2]
                return (second_encounter_cycles, cycle - second_encounter_cycles)
        else:
            seen[key] = [cycle]

def select_entry(memory):
    indexed_memory = list(enumerate(memory)) # zipWithIndex
    selected_entry = reduce(
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
