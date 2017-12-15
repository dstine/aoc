import re

def day12_1(filename):
    return day12(filename)[0]

def day12_2(filename):
    return day12(filename)[1]

def day12(filename):
    lines = readfile(filename)
    programs_dict = parse_lines(lines)
    groups_dict = {}
    while len(programs_dict) > 0:
        seed_program = list(programs_dict.keys())[0]
        groups_dict[seed_program] = find_programs_in_group(programs_dict, seed_program)
    return len(groups_dict[0]), len(groups_dict)

def find_programs_in_group(programs_dict, seed_program):
    programs_to_process = [seed_program]
    programs_in_group = set()
    while len(programs_to_process) > 0:
        program = programs_to_process.pop(0)
        programs_in_group.add(program)
        linked_programs = programs_dict.pop(program, None)
        if linked_programs:
            for linked_program in linked_programs:
                programs_to_process.append(linked_program)
    return programs_in_group

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

def parse_lines(lines):
    programs_dict = {}
    for line in lines:
        parsed = parse_line(line)
        programs_dict[int(parsed[0])] = [int(n) for n in parsed[1]]
    return programs_dict

def parse_line(line):
    program_and_linked_programs = re.search('([0-9]+) <-> ([0-9, ]+)', line)
    if not program_and_linked_programs:
        raise Exception("no match")
    program = program_and_linked_programs.group(1)
    linked_programs = program_and_linked_programs.group(2).split(',')
    return program, linked_programs
