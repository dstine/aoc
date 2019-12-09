const assert = require('assert');

const utils = require('./test_utils.js');
const day08 = require('../day08.js');

describe('day08', function() {
    it('part1-example', function () {
        const digits = '123456789012'.split('').map(Number);
        assert.equal(day08.part1(digits, 3, 2), 1);
    });
    it('part1', function () {
        const digits = utils.get_input('day08', '', Number);
        assert.equal(day08.part1(digits, 25, 6), 1792);
    });
    it('part2-example', function () {
        const digits = '0222112222120000'.split('').map(Number);
        day08.part2(digits, 2, 2);
    });
    it('part2', function () {
        const digits = utils.get_input('day08', '', Number);
        day08.part2(digits, 25, 6);
    });
});
