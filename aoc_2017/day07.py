import re

def day7_1(program_lines):
    programs = [parse_program(program_line) for program_line in program_lines]
    program_names = [program['name'] for program in programs]
    for program in programs:
        for supported in program['supported_names']:
            program_names.remove(supported)
    return program_names[0]

def day7_2(program_lines):
    program_list = [parse_program(program_line) for program_line in program_lines]
    program_dict = {program['name']: program for program in program_list}
    #programs = sorted(parsed_programs, key=lambda p: len(p['supported_names']))
    program_weights = {program['name']: program['weight'] for program in program_list}
    for program in program_list:
        calc_weights(program, program_dict)
    for program in program_list:
        check = check_weights(program, program_dict)
        if check != 0:
            return check
    raise Exception('should never get here')

def calc_weights(program, program_dict):
    if program['supported_weight'] != 0:
        return
    if len(program['supported_names']) == 0:
        program['total_weight'] = program['weight']
        return
    supported_weight = 0
    for supported_name in program['supported_names']:
        supported_program = program_dict[supported_name]
        calc_weights(supported_program, program_dict)
        supported_weight += supported_program['weight'] + supported_program['supported_weight']
    program['supported_weight'] = supported_weight
    program['total_weight'] = program['weight'] + supported_weight

def check_weights(program, program_dict):
    if len(program['supported_names']) == 0:
        return 0
    total_weights = {}
    for supported_name in program['supported_names']:
        supported_program = program_dict[supported_name]
        total_weight = supported_program['total_weight']
        if total_weight in total_weights:
            total_weights[total_weight] += 1
        else:
            total_weights[total_weight] = 1
    if (len(total_weights) == 1):
        return 0
    unbalanced_weight = 0
    balanced_weight = 0
    for weight, count in total_weights.items():
        if count == 1:
            unbalanced_weight = weight
        else:
            balanced_weight = weight
    for supported_name in program['supported_names']:
        supported_program = program_dict[supported_name]
        if supported_program['total_weight'] == unbalanced_weight:
            return supported_program['weight'] - unbalanced_weight + balanced_weight

def parse_program(program_line):
    # program is of the form: name (weight)
    name_and_weight = re.search('([a-z]+) \(([0-9]+)\)', program_line)
    if not name_and_weight:
        raise Exception("no match")
    program_name = name_and_weight.group(1)
    program_weight = name_and_weight.group(2)
    supported_programs = []
    if len(program_line) > name_and_weight.end():
        rest = program_line[name_and_weight.end():]
        supported_programs = re.findall('[a-z]+', rest)
    supported_weight = total_weight = 0
    return {'name': program_name, 'weight': int(program_weight), 
            'supported_weight': supported_weight, 'supported_names': supported_programs,
            'total_weight': total_weight}
