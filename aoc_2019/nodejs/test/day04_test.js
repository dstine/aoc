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
    it('is_candidate2', function () {
        assert.equal(day04.is_candidate2(111111), false);
        assert.equal(day04.is_candidate2(223450), false);
        assert.equal(day04.is_candidate2(123455), true);
        assert.equal(day04.is_candidate2(123789), false);
        assert.equal(day04.is_candidate2(112233), true);
        assert.equal(day04.is_candidate2(123444), false);
        assert.equal(day04.is_candidate2(111122), true);
        
        assert.equal(day04.is_candidate2(111234), false);
        assert.equal(day04.is_candidate2(222211), false);
        assert.equal(day04.is_candidate2(111120), false);
        assert.equal(day04.is_candidate2(201556), false);
        assert.equal(day04.is_candidate2(223456), true);
        assert.equal(day04.is_candidate2(222456), false);
        assert.equal(day04.is_candidate2(113456), true);
        assert.equal(day04.is_candidate2(122456), true);
        assert.equal(day04.is_candidate2(123356), true);
        assert.equal(day04.is_candidate2(123446), true);
        assert.equal(day04.is_candidate2(123455), true);
        assert.equal(day04.is_candidate2(112455), true);
        assert.equal(day04.is_candidate2(122455), true);

        // double followed by triple
        assert.equal(day04.is_candidate2(112225), true);
    });
    it('part2', function () {
        assert.equal(day04.part2('130254-678275'), 1419);
    });
});
