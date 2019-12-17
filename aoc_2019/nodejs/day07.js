const Combinatorics = require('js-combinatorics');
const intcode = require('./intcode.js');

module.exports = {
    part1,
    run_permutation,
    build_amps,
};

class Amp {
    constructor(memory, phase) {
        this.memory = memory;
        this.phase = phase;
    }

    run(input_signal) {
        const outputs = intcode.run_program(this.memory, [this.phase, input_signal]);
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
