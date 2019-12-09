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
});
