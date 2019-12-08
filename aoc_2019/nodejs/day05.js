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
                var val1 = deref(memory, iptr+1, mode1);
                var val2 = deref(memory, iptr+2, mode2);
                var result = val1 + val2;
                memory[decode(memory, iptr+3, mode3)] = result;
                incr = 4;
                break;
            case 2:
                if (debug) console.log('op2');
                var val1 = deref(memory, iptr+1, mode1);
                var val2 = deref(memory, iptr+2, mode2);
                var result = val1 * val2;
                memory[decode(memory, iptr+3, mode3)] = result;
                incr = 4;
                break;
            case 3:
                if (debug) console.log('op3');
                memory[decode(memory, iptr+1, mode1)] = input;
                incr = 2;
                break;
            case 4:
                if (debug) console.log('op4');
                var output = deref(memory, iptr+1, mode1);
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

function deref(memory, iptr, mode) {
    return memory[decode(memory, iptr, mode)];
}

function decode(memory, iptr, mode) {
    return mode ? iptr : memory[iptr];
}

function part1(memory) {
    return run_program(memory, 1);
}
