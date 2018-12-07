from collections import defaultdict

def part1(instructions):
    step_graph = defaultdict(set)

    instructions = parse(instructions)
    for inst in instructions:
        step = inst[1]
        predecessor = inst[0]
        step_graph[predecessor]
        step_graph[step].add(predecessor)

    ordered = []
    while len(step_graph) > 0:
        next = next_step(step_graph)
        ordered.append(next)
        remove_step(step_graph, next)
    return ''.join(ordered)

def parse(instructions):
    parsed = [inst.split(' ') for inst in instructions]
    return [(p[1], p[7]) for p in parsed]

def next_step(step_graph):
    available = [step for step, predecessors in step_graph.items() if len(predecessors) == 0]
    return sorted(available)[0]

def remove_step(step_graph, step):
    step_graph.pop(step)
    for predecessors in step_graph.values():
        predecessors.discard(step)
