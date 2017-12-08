import re

def day7_1(programs):
    parsed = [parse_program(program) for program in programs]
    program_names = [p[0] for p in parsed]
    for p in parsed:
        for supported in p[2]:
            program_names.remove(supported)
    return program_names[0]

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

def parse_program(program):
    # program is of the form: name (weight)
    name_and_weight = re.search('([a-z]+) \(([0-9]+)\)', program)
    if not name_and_weight:
        raise Exception("no match")
    program_name = name_and_weight.group(1)
    program_weight = name_and_weight.group(2)
    supported_programs = []
    if len(program) > name_and_weight.end():
        rest = program[name_and_weight.end():]
        supported_programs = re.findall('[a-z]+', rest)
    return (program_name, program_weight, supported_programs)
