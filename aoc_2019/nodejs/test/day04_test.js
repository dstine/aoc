var assert = require('assert');

var day04 = require('../day04.js');

describe('day04', function() {
    it('is_candidate', function () {
        assert.equal(day04.is_candidate(111111), true);
        assert.equal(day04.is_candidate(223450), false);
        assert.equal(day04.is_candidate(123455), true);
        assert.equal(day04.is_candidate(123789), false);
    });
    it('part1', function () {
        assert.equal(day04.part1('130254-678275'), 2090);
    });
});
