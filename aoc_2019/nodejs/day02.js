module.exports = {
    run_program: run_program,
    part1: part1,
    part2: part2,
};

function run_program(opcodes) {
    var pc = 0;
    while (pc < opcodes.length) {
        var opcode = opcodes[pc];
        switch (opcode) {
            case 1:
                opcodes[opcodes[pc+3]] = opcodes[opcodes[pc+1]] + opcodes[opcodes[pc+2]];
                break;
            case 2:
                opcodes[opcodes[pc+3]] = opcodes[opcodes[pc+1]] * opcodes[opcodes[pc+2]];
                break;
            case 99:
                return opcodes[0];
            default:
                throw `unknown opcode: ${opcode}`;
        }
        pc += 4;
    }
    return opcodes[0];
}

function part1(opcodes) {
    opcodes[1] = 12;
    opcodes[2] = 2;
    return run_program(opcodes);
}

function part2(opcodes, target) {
    for (var noun=0; noun<100; noun++) {
        for (var verb=0; verb<100; verb++) {
            var ops = [...opcodes];
            ops[1] = noun;
            ops[2] = verb;
            var result = run_program(ops);
            if (result == target) {
                return 100 * noun + verb;
            }
        }
    }
    return -1;
}
