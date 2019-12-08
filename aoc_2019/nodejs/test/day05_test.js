const assert = require('assert');

const utils = require('./test_utils.js');
const day05 = require('../day05.js');

describe('day05', function() {
    it('run_program_ops34', function () {
        assert.deepEqual(day05.run_program([1002,4,3,4,33], 123456), []);
    });
    it('part1', function () {
        const memory = utils.get_input('day05', ',', Number);
        assert.deepEqual(day05.part1(memory), [0, 0, 0, 0, 0, 0, 0, 0, 0, 6069343]);
    });
    it('run_program_ops78', function () {
        assert.deepEqual(day05.run_program([3,9,8,9,10,9,4,9,99,-1,8], 7), [0]);
        assert.deepEqual(day05.run_program([3,9,8,9,10,9,4,9,99,-1,8], 8), [1]);
        assert.deepEqual(day05.run_program([3,9,8,9,10,9,4,9,99,-1,8], 9), [0]);

        assert.deepEqual(day05.run_program([3,9,7,9,10,9,4,9,99,-1,8], 7), [1]);
        assert.deepEqual(day05.run_program([3,9,7,9,10,9,4,9,99,-1,8], 8), [0]);
        assert.deepEqual(day05.run_program([3,9,7,9,10,9,4,9,99,-1,8], 9), [0]);

        assert.deepEqual(day05.run_program([3,3,1108,-1,8,3,4,3,99], 7), [0]);
        assert.deepEqual(day05.run_program([3,3,1108,-1,8,3,4,3,99], 8), [1]);
        assert.deepEqual(day05.run_program([3,3,1108,-1,8,3,4,3,99], 9), [0]);

        assert.deepEqual(day05.run_program([3,3,1107,-1,8,3,4,3,99], 7), [1]);
        assert.deepEqual(day05.run_program([3,3,1107,-1,8,3,4,3,99], 8), [0]);
        assert.deepEqual(day05.run_program([3,3,1107,-1,8,3,4,3,99], 9), [0]);
    });
    it('run_program_ops56', function () {
        assert.deepEqual(day05.run_program([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0), [0]);
        assert.deepEqual(day05.run_program([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1), [1]);
        assert.deepEqual(day05.run_program([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0), [0]);
        assert.deepEqual(day05.run_program([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1), [1]);

    });
    it('run_program_larger', function () {
        const memory = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99];
        assert.deepEqual(day05.run_program(memory, 7), [999]);
        assert.deepEqual(day05.run_program(memory, 8), [1000]);
        assert.deepEqual(day05.run_program(memory, 9), [1001]);
    });
    it('part2', function () {
        const memory = utils.get_input('day05', ',', Number);
        assert.deepEqual(day05.part2(memory), [3188550]);
    });
});
