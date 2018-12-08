def part1(nums):
    _, total = explore_node(nums)
    return total

def explore_node(nums):
    n_children = nums[0]
    n_metadata = nums[1]
    total = 0
    i = 2
    for _ in range(n_children):
        sub_i, subtotal = explore_node(nums[i:])
        i += sub_i
        total += subtotal
    for _ in range(n_metadata):
        metadata = nums[i]
        total += metadata
        i += 1
    return i, total
