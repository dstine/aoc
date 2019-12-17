const assert = require('assert');

const utils = require('./test_utils.js');
const day02 = require('../day02.js');

describe('day02', function() {
    it('part1', function () {
        const memory = utils.get_input('day02', ',', Number);
        assert.equal(day02.part1(memory), 7210630);
    });
    it('part2', function () {
        const memory = utils.get_input('day02', ',', Number);
        assert.equal(day02.part2(memory, 19690720), 3892);
    });
});
