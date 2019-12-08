module.exports = {
    run_program: run_program,
    part1: part1,
    // part2: part2,
};

var debug = false;

function run_program(memory, input) {
    var outputs = [];
    var iptr = 0;
    var incr = 0;
    var halt = false;
    while (iptr < memory.length && !halt) {
        var iword = memory[iptr];
        var opcode = iword % 1e2;
        var mode1 = Math.trunc(iword / 1e2) % 10;
        var mode2 = Math.trunc(iword / 1e3) % 10;
        var mode3 = Math.trunc(iword / 1e4) % 10;
        switch (opcode) {
            case 1:
                if (debug) console.log('op1');
                var val1 = mode1 ? memory[iptr+1] : memory[memory[iptr+1]];
                var val2 = mode2 ? memory[iptr+2] : memory[memory[iptr+2]];
                var result = val1 + val2;
                if (mode3) {
                    memory[iptr+3] = result;
                } else {
                    memory[memory[iptr+3]] = result;
                }
                incr = 4;
                break;
            case 2:
                if (debug) console.log('op2');
                var val1 = mode1 ? memory[iptr+1] : memory[memory[iptr+1]];
                var val2 = mode2 ? memory[iptr+2] : memory[memory[iptr+2]];
                var result = val1 * val2;
                if (mode3) {
                    memory[iptr+3] = result;
                } else {
                    memory[memory[iptr+3]] = result;
                }
                incr = 4;
                break;
            case 3:
                if (debug) console.log('op3');
                if (mode1) {
                    memory[iptr+1] = input;
                } else {
                    memory[memory[iptr+1]] = input;
                }
                incr = 2;
                break;
            case 4:
                if (debug) console.log('op4');
                var output = mode1 ? memory[iptr+1] : memory[memory[iptr+1]];
                outputs.push(output);
                incr = 2;
                break;
            case 99:
                if (debug) console.log('op99');
                halt = true;
                break;
            default:
                throw `unknown opcode: ${opcode}`;
        }
        iptr += incr;
    }
    var diagnostic_code = memory[0];
    outputs.push(diagnostic_code);
    return outputs;
}

function part1(memory) {
    return run_program(memory, 1);
}
