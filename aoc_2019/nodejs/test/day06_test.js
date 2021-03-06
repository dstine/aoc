const assert = require('assert');

const utils = require('./test_utils.js');
const day06 = require('../day06.js');

describe('day06', function() {
    it('part1-example', function () {
        let map = utils.get_example('day06', '\n', String);
        assert.deepEqual(day06.part1(map), 42);
        map = utils.get_example('day06', '\n', String, '_unsorted');
        assert.deepEqual(day06.part1(map), 42);
    });
    it('part1', function () {
        const map = utils.get_input('day06', '\n', String);
        assert.deepEqual(day06.part1(map), 117672);
    });
    it('part2-example', function () {
        let map = utils.get_example('day06', '\n', String, '_transfers');
        assert.deepEqual(day06.part2(map), 4);
    });
    it('part2', function () {
        let map = utils.get_input('day06', '\n', String);
        assert.deepEqual(day06.part2(map), 277);
    });
});
