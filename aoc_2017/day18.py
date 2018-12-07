from collections import defaultdict

def part1(instructions):
    sound = -1
    regs = defaultdict(int)
    pc = 0
    instructions = [inst.split(' ') for inst in instructions]
    while True:
        inst = instructions[pc]
        op = inst[0]
        reg = inst[1]

        #msg = '{} {} {}'.format(pc, op, reg)
        #if 'a' in regs:
        #    msg = str(regs['a']) + ': ' + msg
        #else:
        #    msg = ' : ' + msg
        #if len(inst) == 3:
        #    msg += ' ' + inst[2]
        #print(msg)

        if op == 'snd':
            # plays a sound with a frequency equal to the value of X.
            sound = regs[reg]
            pc += 1
        elif op == 'set':
            # sets register X to the value of Y.
            y = value(inst[2], regs)
            regs[reg] = y
            pc += 1
        elif op == 'add':
            # increases register X by the value of Y.
            y = value(inst[2], regs)
            regs[reg] += y
            pc += 1
        elif op == 'mul':
            # sets register X to the result of multiplying the value contained in register X by the value of Y.
            y = value(inst[2], regs)
            regs[reg] *= y
            pc += 1
        elif op == 'mod':
            # sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
            y = value(inst[2], regs)
            regs[reg] %= y
            pc += 1
        elif op == 'rcv':
            # recovers the frequency of the last sound played, but only when the value of X is not zero.
            # (If it is zero, the command does nothing.)
            if regs[reg] !=0:
                return sound
            pc += 1
        elif op == 'jgz':
            # jumps with an offset of the value of Y, but only if the value of X is greater than zero.
            # (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
            if regs[reg] > 0:
                y = value(inst[2], regs)
                pc += y
            else:
                pc += 1

def value(s, regs):
    s_abs = s.replace('-', '')
    if s_abs.isnumeric():
        return int(s)
    else:
        return regs[s]
