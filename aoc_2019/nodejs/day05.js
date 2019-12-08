module.exports = {
    run_program: run_program,
    part1: part1,
    part2: part2,
};

var debug = false;

function run_program(memory, input) {
    var outputs = [];
    var iptr = 0;
    var halt = false;
    while (iptr < memory.length && !halt) {
        var iword = memory[iptr];
        var opcode = iword % 1e2;
        var modes = Math.trunc(iword / 1e2);
        if (debug) {
            console.log('--------------');
            console.log(`memory ${memory}`);
            console.log(`iptr   ${iptr}`);
            console.log(`op     ${opcode}`);
        }
        if ([1,2,7,8].includes(opcode)) {
            var val1 = deref(memory, iptr, modes, 1);
            var val2 = deref(memory, iptr, modes, 2);
            var result_loc = decode(memory, iptr, modes, 3);
            if (1 == opcode) {
                memory[result_loc] = val1 + val2;
            } else if (2 == opcode) {
                memory[result_loc] = val1 * val2;
            } else if (7 == opcode) {
                memory[result_loc] = val1 < val2 ? 1 : 0;
            } else if (8 == opcode) {
                memory[result_loc] = val1 == val2 ? 1 : 0;
            }
            iptr += 4;
        } else if (3 == opcode) {
            memory[decode(memory, iptr, modes, 1)] = input;
            iptr += 2;
        } else if (4 == opcode) {
            var output = deref(memory, iptr, modes, 1);
            outputs.push(output);
            iptr += 2;
        } else if (5 == opcode) {
            val1 = deref(memory, iptr, modes, 1);
            if (val1) {
                iptr = deref(memory, iptr, modes, 2);
            } else {
                iptr += 3;
            }
        } else if (6 == opcode) {
            val1 = deref(memory, iptr, modes, 1);
            if (val1 == 0) {
                iptr = deref(memory, iptr, modes, 2);
            } else {
                iptr += 3;
            }
        } else if (99 == opcode) {
            halt = true;
        } else {
            throw `unknown opcode: ${opcode}`;
        }
    }
    var diagnostic_code = memory[0];
    outputs.push(diagnostic_code);
    return outputs;
}

function deref(memory, iptr, modes, offset) {
    return memory[decode(memory, iptr, modes, offset)];
}

function decode(memory, iptr, modes, offset) {
    var mode = Math.trunc(modes / Math.pow(10, offset-1)) % 10;
    return mode ? iptr+offset : memory[iptr+offset];
}

function part1(memory) {
    return run_program(memory, 1);
}

function part2(memory) {
    return run_program(memory, 5);
}
