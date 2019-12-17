const assert = require('assert');

const utils = require('./test_utils.js');
const day05 = require('../day05.js');

describe('day05', function() {
    it('part1', function () {
        const memory = utils.get_input('day05', ',', Number);
        assert.deepEqual(day05.part1(memory), [0, 0, 0, 0, 0, 0, 0, 0, 0, 6069343]);
    });
    it('part2', function () {
        const memory = utils.get_input('day05', ',', Number);
        assert.deepEqual(day05.part2(memory), [3188550]);
    });
});
