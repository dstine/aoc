module.exports = {
    run_program,
    part1,
    part2,
};

function run_program(memory) {
    var iptr = 0;
    var halt = false;
    while (iptr < memory.length && !halt) {
        var opcode = memory[iptr];
        switch (opcode) {
            case 1:
                memory[memory[iptr+3]] = memory[memory[iptr+1]] + memory[memory[iptr+2]];
                break;
            case 2:
                memory[memory[iptr+3]] = memory[memory[iptr+1]] * memory[memory[iptr+2]];
                break;
            case 99:
                halt = true;
                break;
            default:
                throw `unknown opcode: ${opcode}`;
        }
        iptr += 4;
    }
    return memory[0];
}

function part1(memory) {
    memory[1] = 12;
    memory[2] = 2;
    return run_program(memory);
}

function part2(memory, target) {
    for (var noun=0; noun<100; noun++) {
        for (var verb=0; verb<100; verb++) {
            var mem = [...memory];
            mem[1] = noun;
            mem[2] = verb;
            var result = run_program(mem);
            if (result == target) {
                return 100 * noun + verb;
            }
        }
    }
    return -1;
}
