const assert = require('assert');

const utils = require('./test_utils.js');
const day06 = require('../day06.js');

describe('day06', function() {
    it('count_orbits', function () {
        let map = utils.get_example('day06', '\n', String);
        assert.deepEqual(day06.count_orbits(map), 42);
        map = utils.get_example('day06', '\n', String, '_unsorted');
        assert.deepEqual(day06.count_orbits(map), 42);
    });
    it('part1', function () {
        const map = utils.get_input('day06', '\n', String);
        assert.deepEqual(day06.count_orbits(map), 117672);
    });
});
