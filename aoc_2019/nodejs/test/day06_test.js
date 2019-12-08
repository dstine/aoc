var assert = require('assert');

var utils = require('./test_utils.js');
var day06 = require('../day06.js');

describe('day06', function() {
    it('count_orbits', function () {
        var map = utils.get_example('day06', '\n', String);
        assert.deepEqual(day06.count_orbits(map), 42);
        console.log('----------------------')
        var map = utils.get_example('day06', '\n', String, '_unsorted');
        assert.deepEqual(day06.count_orbits(map), 42);
    });
    it('part1', function () {
        var map = utils.get_input('day06', '\n', String);
        assert.deepEqual(day06.count_orbits(map), 117672);
    });
});
