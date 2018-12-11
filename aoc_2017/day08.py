import re

def day8_1(program_lines):
    return day8(program_lines)[0]

def day8_2(program_lines):
    return day8(program_lines)[1]

def day8(program_lines):
    instructions = [parse_instruction(program_line) for program_line in program_lines]
    register_names = set([instruction['register'] for instruction in instructions])
    registers = {name: 0 for name in register_names}
    max_ever_value = 0
    for instruction in instructions:
        register = instruction['register']
        register_value = registers[register]
        operation = instruction['operation']
        operation = operation.replace('inc', '+').replace('dec', '-')
        value = instruction['value']
        pred_register = registers[instruction['pred_register']]
        pred_operator = instruction['pred_operator']
        pred_value = instruction['pred_value']
        predicate = eval("{} {} {}".format(pred_register, pred_operator, pred_value))
        if predicate:
            new_value = eval("{} {} {}".format(register_value, operation, value))
            registers[register] = new_value
            if new_value > max_ever_value:
                max_ever_value = new_value
    max_current_value = max(registers.values())
    return (max_current_value, max_ever_value)

def parse_instruction(program_line):
    match = re.search(r'([a-z]+) ([a-z]+) ([-0-9]+) if ([a-z]+) ([<>=!]+) ([-0-9]+)', program_line)
    if not match:
        raise Exception("no match")
    register = match.group(1)
    operation = match.group(2)
    value = match.group(3)
    pred_register = match.group(4)
    pred_operator = match.group(5)
    pred_value = match.group(6)
    return {
        'register': register,
        'operation': operation,
        'value': int(value),
        'pred_register': pred_register,
        'pred_operator': pred_operator,
        'pred_value': int(pred_value)
    }

def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]
