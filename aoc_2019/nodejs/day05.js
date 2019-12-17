const intcode = require('./intcode.js');

module.exports = {
    part1,
    part2,
};

function part1(memory) {
    return intcode.run_program(memory, [1]);
}

function part2(memory) {
    return intcode.run_program(memory, [5]);
}
