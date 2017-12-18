import re

SCANNER = 1
EMPTY = 0

POSITIVE = 'P'
NEGATIVE = 'N'

def day13_1(filename):
    lines = readfile(filename)
    layers_dict = parse_lines(lines)
    firewall = {layer[0]: Layer(POSITIVE, [SCANNER] + [EMPTY] * (layer[1]-1)) for layer in layers_dict.items()}
    packet_layer = 0
    firewall_depth = max(firewall)+1
    severity = 0
    for _ in range(firewall_depth):
        if packet_layer in firewall:
            if firewall[packet_layer].locations[0] == 1:
                severity += packet_layer * len(firewall[packet_layer].locations)
        tick_picosecond(firewall)
        packet_layer += 1
    return severity

def tick_picosecond(firewall):
    for layer in firewall:
        direction = firewall[layer].direction
        locations = firewall[layer].locations
        scanner_idx = locations.index(SCANNER)
        if direction == POSITIVE:
            if scanner_idx < len(locations) - 1:
                move_positive(locations, scanner_idx)
            else:
                move_negative(locations, scanner_idx)
                firewall[layer].direction = NEGATIVE
        if direction == NEGATIVE:
            if scanner_idx > 0:
                move_negative(locations, scanner_idx)
            else:
                move_positive(locations, scanner_idx)
                firewall[layer].direction = POSITIVE

def move_positive(locations, scanner_idx):
    locations[scanner_idx] = EMPTY
    locations[scanner_idx+1] = SCANNER

def move_negative(locations, scanner_idx):
    locations[scanner_idx] = EMPTY
    locations[scanner_idx-1] = SCANNER

def day13_2(filename):
    lines = readfile(filename)
    layers_dict = parse_lines(lines)
    delay = 0
    while True:
        if not caught(layers_dict, delay):
            return delay
        delay += 1

def caught(layers_dict, delay):
    packet_layer = 0
    for n in range(max(layers_dict) + 1):
        if packet_layer in layers_dict:
            if scanner_location(delay + packet_layer, layers_dict[packet_layer]) == 0:
                return True
        packet_layer += 1
    return False

def scanner_location(time, depth):
    return time % (2*depth - 2)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

def parse_lines(lines):
    layers_dict = {}
    for line in lines:
        parsed = parse_line(line)
        layers_dict[int(parsed[0])] = int(parsed[1])
    return layers_dict

def parse_line(line):
    depth_and_range = re.search('([0-9]+): ([0-9]+)', line)
    if not depth_and_range:
        raise Exception("no match")
    depth = depth_and_range.group(1)
    range = depth_and_range.group(2)
    return depth, range

class Layer(object):
    direction = POSITIVE
    locations = []
    def __init__(self, direction, locations):
        self.direction = direction
        self.locations = locations
    def __repr__(self):
        return "dir: {}, locs: {}".format(self.direction, self.locations)
