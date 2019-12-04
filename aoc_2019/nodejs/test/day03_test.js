var assert = require('assert');

var utils = require('./test_utils.js');
var day03 = require('../day03.js');

describe('day03', function() {
    it('walk', function () {
        var w1_moves = ['R8','U5','L5','D3'];
        var w1_actual = day03.walk(w1_moves);
        var w1_expected = [
                [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0],
                [8,1], [8,2], [8,3], [8,4], [8,5],
                [7,5], [6,5], [5,5], [4,5], [3,5],
                [3,4], [3,3], [3,2],
            ];
        assert.deepEqual(w1_actual, w1_expected);
    });
    it('dist', function () {
        assert.equal(day03.dist([3,3], [6,6]), 6);
        assert.equal(day03.dist([-3,-3], [6,6]), 18);
        assert.equal(day03.dist([1,2], [-6,1]), 8);
    });
    it('intersection', function () {
        var w1_moves = ['R8','U5','L5','D3'];
        var w2_moves = ['U7','R6','D4','L4'];
        var actual = day03.intersection(w1_moves, w2_moves);
        var expected = [[6,5], [3,3]];
        assert.deepEqual(actual, expected);
    });
    it('part1-example', function () {
        var w1_moves = ['R8','U5','L5','D3'];
        var w2_moves = ['U7','R6','D4','L4'];
        assert.equal(day03.part1(w1_moves, w2_moves), 6);
    });
    it('part1', function () {
        var moves = utils.get_input('day03');
        var w1_moves = moves[0].split(',');
        var w2_moves = moves[1].split(',');
        assert.equal(day03.part1(w1_moves, w2_moves), 1431);
    });
});
