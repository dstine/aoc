from collections import defaultdict

def part1(instructions):
    steps = order_steps(instructions)
    return ''.join(steps)

def part2(instructions, n, base_time):
    graph = build_graph(instructions)
    workers = [['', 0] for _ in range(n)]
    t = 0
    while True:
        # do work
        for i, worker in enumerate(workers):
            assigned_step = worker[0]
            if assigned_step != '':
                worker[1] -= 1
                if worker[1] == 0:
                    remove_step(graph, assigned_step)
                    workers[i] = ['', 0]

        # assign work
        available_steps = find_available_steps(graph)
        available_workers = find_available_workers(workers)
        bound = min(len(available_steps), len(available_workers))
        for i, (available_step, available_worker) in enumerate(zip(available_steps, available_workers)):
            if i == bound:
                break
            available_worker[0] = available_step
            available_worker[1] = cost(available_step, base_time)
            graph[available_step]['status'] = 'I'

        if len(graph) == 0:
            return t
        t += 1

def order_steps(instructions):
    graph = build_graph(instructions)
    ordered = []
    while len(graph) > 0:
        next = next_step(graph)
        ordered.append(next)
        remove_step(graph, next)
    return ordered

def build_graph(instructions):
    # graph is a dict
    #     key: step
    #     value: dict of 'predecessors' and 'status'
    #            status in {'U', 'I'} (Unassigned, In-Progress)
    graph = defaultdict(lambda: {'predecessors': set(), 'status': 'U'})
    instructions = parse(instructions)
    for inst in instructions:
        step = inst[1]
        predecessor = inst[0]
        graph[predecessor]
        graph[step]['predecessors'].add(predecessor)
    return graph

def parse(instructions):
    parsed = [inst.split(' ') for inst in instructions]
    return [(p[1], p[7]) for p in parsed]

def next_step(graph):
    available = []
    for step, vals in graph.items():
        if len(vals['predecessors']) == 0:
            available.append(step)
    return sorted(available)[0]

def remove_step(graph, step):
    graph.pop(step)
    for val in graph.values():
        val['predecessors'].discard(step)

def find_available_steps(graph):
    available = []
    for step, vals in graph.items():
        if vals['predecessors'] == set() and vals['status'] == 'U':
            available.append(step)
    return available

def find_available_workers(workers):
    available = []
    for worker in workers:
        if worker[0] == '':
            available.append(worker)
    return available

def cost(step, base_time):
    return ord(step) - ord('A') + 1 + base_time
