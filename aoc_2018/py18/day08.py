def part1(nums):
    _, total, _ = explore_node(nums)
    return total

def part2(nums):
    _, _, value = explore_node(nums)
    return value

def explore_node(nums):
    n_children = nums[0]
    n_metadata = nums[1]
    total = 0
    i = 2

    children = []
    for _ in range(n_children):
        child_i, child_total, child_value = explore_node(nums[i:])
        i += child_i
        total += child_total
        children.append(child_value)

    metadata = []
    for _ in range(n_metadata):
        child_cardinal = nums[i]
        total += child_cardinal
        i += 1
        metadata.append(child_cardinal)

    value = 0
    if len(children) == 0:
        value = sum(metadata)
    else:
        for child_cardinal in metadata:
            child_index = child_cardinal-1
            if child_index < len(children):
                value += children[child_index]

    return i, total, value
