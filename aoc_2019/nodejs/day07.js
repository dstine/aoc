const Combinatorics = require('js-combinatorics');

module.exports = {
    part1,
    run_permutation,
    run_program,
};

function part1(memory) {
    const permutations = Combinatorics.permutation([0,1,2,3,4]).toArray();
    let max_signal = 0;
    for (let i=0; i <permutations.length; i++) {
        const phases = permutations[i];
        const signal = run_permutation(memory, phases);
        max_signal = Math.max(max_signal, signal);
    }
    return max_signal;
}

function run_permutation(memory, phases) {
    let signal = 0;
    for (let i=0; i<phases.length; i++) {
        const mem = [...memory];
        const outputs = run_program(mem, [phases[i], signal]);
        signal = outputs.pop();
    }
    return signal;
}

const debug = false;

function run_program(memory, inputs) {
    if (debug) {
        console.log('==============');
        console.log(`inputs ${inputs}`);
    }
    const outputs = [];
    let iptr = 0;
    let halt = false;
    while (iptr < memory.length && !halt) {
        const iword = memory[iptr];
        const opcode = iword % 1e2;
        const modes = Math.trunc(iword / 1e2);
        if (debug) {
            console.log('  --------------');
            console.log(`  memory ${memory}`);
            console.log(`  iptr   ${iptr}`);
            console.log(`  op     ${opcode}`);
        }
        if ([1,2,7,8].includes(opcode)) {
            const val1 = deref(memory, iptr, modes, 1);
            const val2 = deref(memory, iptr, modes, 2);
            const result_loc = decode(memory, iptr, modes, 3);
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
            memory[decode(memory, iptr, modes, 1)] = inputs.shift();
            iptr += 2;
        } else if (4 == opcode) {
            const output = deref(memory, iptr, modes, 1);
            outputs.push(output);
            iptr += 2;
        } else if (5 == opcode) {
            const val1 = deref(memory, iptr, modes, 1);
            if (val1) {
                iptr = deref(memory, iptr, modes, 2);
            } else {
                iptr += 3;
            }
        } else if (6 == opcode) {
            const val1 = deref(memory, iptr, modes, 1);
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
    return outputs;
}

function deref(memory, iptr, modes, offset) {
    return memory[decode(memory, iptr, modes, offset)];
}

function decode(memory, iptr, modes, offset) {
    const mode = Math.trunc(modes / Math.pow(10, offset-1)) % 10;
    return mode ? iptr+offset : memory[iptr+offset];
}
