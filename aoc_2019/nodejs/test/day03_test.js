const assert = require('assert');

const utils = require('./test_utils.js');
const day03 = require('../day03.js');

describe('day03', function() {
    it('walk', function () {
        const w1_moves = ['R8','U5','L5','D3'];
        const w1_actual = day03.walk(w1_moves);
        const w1_expected = [
                [1,0,1], [2,0,2], [3,0,3], [4,0,4], [5,0,5], [6,0,6], [7,0,7], [8,0,8],
                [8,1,9], [8,2,10], [8,3,11], [8,4,12], [8,5,13],
                [7,5,14], [6,5,15], [5,5,16], [4,5,17], [3,5,18],
                [3,4,19], [3,3,20], [3,2,21],
            ].map(t => new day03.Point(t[0], t[1], t[2]));
        assert.deepEqual(w1_actual, w1_expected);
    });
    it('dist', function () {
        assert.equal(day03.dist(new day03.Point(3,3), new day03.Point(6,6)), 6);
        assert.equal(day03.dist(new day03.Point(-3,-3), new day03.Point(6,6)), 18);
        assert.equal(day03.dist(new day03.Point(1,2), new day03.Point(-6,1)), 8);
    });
    it('intersection', function () {
        const w1_moves = ['R8','U5','L5','D3'];
        const w2_moves = ['U7','R6','D4','L4'];
        const actual = day03.intersection(w1_moves, w2_moves);
        const expected = [
            [new day03.Point(6,5,15), new day03.Point(6,5,15)],
            [new day03.Point(3,3,20), new day03.Point(3,3,20)]
        ];
        assert.deepEqual(actual, expected);
    });
    it('part1-example', function () {
        let w1_moves = ['R8','U5','L5','D3'];
        let w2_moves = ['U7','R6','D4','L4'];
        assert.equal(day03.part1(w1_moves, w2_moves), 6);
        w1_moves = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',');
        w2_moves = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',');
        assert.equal(day03.part1(w1_moves, w2_moves), 159);
        w1_moves = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',');
        w2_moves = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',');
        assert.equal(day03.part1(w1_moves, w2_moves), 135);
    });
    it('part1', function () {
        this.timeout(200000);
        const moves = utils.get_input('day03');
        const w1_moves = moves[0].split(',');
        const w2_moves = moves[1].split(',');
        assert.equal(day03.part1(w1_moves, w2_moves), 1431);
    });
    it('part2-example', function () {
        let w1_moves = ['R8','U5','L5','D3'];
        let w2_moves = ['U7','R6','D4','L4'];
        assert.equal(day03.part2(w1_moves, w2_moves), 30);
        w1_moves = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',');
        w2_moves = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',');
        assert.equal(day03.part2(w1_moves, w2_moves), 610);
        w1_moves = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',');
        w2_moves = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',');
        assert.equal(day03.part2(w1_moves, w2_moves), 410);
    });
    it('part2', function () {
        this.timeout(200000);
        const moves = utils.get_input('day03');
        const w1_moves = moves[0].split(',');
        const w2_moves = moves[1].split(',');
        assert.equal(day03.part2(w1_moves, w2_moves), 48012);
    });
});
