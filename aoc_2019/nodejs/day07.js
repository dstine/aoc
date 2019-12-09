const Combinatorics = require('js-combinatorics');

module.exports = {
    part1,
    run_permutation,
    build_amps,
    run_program,
};

class Amp {
    constructor(memory, phase) {
        this.memory = memory;
        this.phase = phase;
    }

    run(input_signal) {
        const outputs = run_program(this.memory, [this.phase, input_signal]);
        const output_signal = outputs.pop();
        return output_signal;
    }
}

function part1(memory) {
    const permutations = Combinatorics.permutation([0,1,2,3,4]).toArray();
    return permutations.reduce(
        (max_signal, phases) => {
            const amps = build_amps(memory, phases);
            const signal = run_permutation(amps);
            return Math.max(max_signal, signal);
        }, 0);
}

function run_permutation(amps) {
    return amps.reduce((signal, amp) => amp.run(signal), 0);
}

function build_amps(memory, phases) {
    return phases.map(phase => {
        const mem = [...memory];
        return new Amp(mem, phase);
    });
}

/****************************
 * IntCode Computer
 ****************************/

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
