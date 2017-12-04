import math

def day3_1(num):
    if num == 1:
        return 0
        
    ring_edge_len = ring_edge(num)
    modulus = ring_edge_len - 1
    vals = []
    increment = 1
    val = modulus - 1
    for _ in range(0, modulus):
        vals.append(val)
        val += increment
        if val == modulus:
            increment = -1
        if val == modulus // 2:
            increment = 1

    idx = num % modulus
    return vals[idx]

def ring_edge(num):
    ring_edge_len = int(math.ceil(math.sqrt(num)))
    if ring_edge_len % 2 == 0:
        ring_edge_len += 1
    return ring_edge_len
