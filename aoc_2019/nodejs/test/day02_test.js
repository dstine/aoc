const assert = require('assert');

const utils = require('./test_utils.js');
const day02 = require('../day02.js');

describe('day02', function() {
    it('run_program', function () {
        assert.equal(day02.run_program([1,9,10,3,2,3,11,0,99,30,40,50]), 3500);
        assert.equal(day02.run_program([1,0,0,0,99]), 2);
        assert.equal(day02.run_program([2,3,0,3,99]), 2);
        assert.equal(day02.run_program([2,4,4,5,99,0]), 2);
        assert.equal(day02.run_program([1,1,1,4,99,5,6,0,99]), 30);
    });
    it('part1', function () {
        const memory = utils.get_input('day02', ',', Number);
        assert.equal(day02.part1(memory), 7210630);
    });
    it('part2', function () {
        const memory = utils.get_input('day02', ',', Number);
        assert.equal(day02.part2(memory, 19690720), 3892);
    });
});
