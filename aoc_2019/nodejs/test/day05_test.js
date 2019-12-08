var assert = require('assert');

var utils = require('./test_utils.js');
var day05 = require('../day05.js');

describe('day02', function() {
    it('run_program', function () {
        assert.deepEqual(day05.run_program([1002,4,3,4,33], 123456), [1002]);
    });
    it('part1', function () {
        var memory = utils.get_input('day05', ',', Number);
        // TODO: why is there a trailing 3?
        assert.deepEqual(day05.part1(memory), [0, 0, 0, 0, 0, 0, 0, 0, 0, 6069343, 3]);
    });
});
