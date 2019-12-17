const intcode = require('./intcode.js');

module.exports = {
    part1,
    part2,
};

function part1(memory) {
    memory[1] = 12;
    memory[2] = 2;
    intcode.run_program(memory);
    return memory[0];
}

function part2(memory, target) {
    for (let noun=0; noun<100; noun++) {
        for (let verb=0; verb<100; verb++) {
            const mem = [...memory];
            mem[1] = noun;
            mem[2] = verb;
            intcode.run_program(mem);
            const result = mem[0];
            if (result == target) {
                return 100 * noun + verb;
            }
        }
    }
    return -1;
}
