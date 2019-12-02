var assert = require('assert');

var utils = require('./test_utils.js');
var day02 = require('../day02.js');

describe('day02', function() {
    it('run_program', function () {
        assert.equal(day02.run_program([1,9,10,3,2,3,11,0,99,30,40,50]), 3500);
        assert.equal(day02.run_program([1,0,0,0,99]), 2);
        assert.equal(day02.run_program([2,3,0,3,99]), 2);
        assert.equal(day02.run_program([2,4,4,5,99,0]), 2);
        assert.equal(day02.run_program([1,1,1,4,99,5,6,0,99]), 30);
    });
    it('part1', function () {
        var opcodes = utils.get_input('day02', ',');
        assert.equal(day02.part1(opcodes), 7210630);
    });
});
