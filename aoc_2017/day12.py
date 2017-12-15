import re

def day12_1(filename):
    lines = readfile(filename)
    dict = parse_lines(lines)
    programs_to_process = [0]
    return process_group(dict, programs_to_process)

def process_group(dict, programs_to_process):
    programs_in_group = set()
    while len(programs_to_process) > 0:
        program = programs_to_process.pop(0)
        programs_in_group.add(program)
        linked_programs = dict.pop(program, None)
        if linked_programs:
            for linked_program in linked_programs:
                programs_to_process.append(linked_program)
    return len(programs_in_group)

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

def parse_lines(lines):
    dict = {}
    for line in lines:
        parsed = parse_line(line)
        dict[int(parsed[0])] = [int(n) for n in parsed[1]]
    return dict

def parse_line(line):
    program_and_linked_programs = re.search('([0-9]+) <-> ([0-9, ]+)', line)
    if not program_and_linked_programs:
        raise Exception("no match")
    program = program_and_linked_programs.group(1)
    linked_programs = program_and_linked_programs.group(2).split(',')
    return program, linked_programs
