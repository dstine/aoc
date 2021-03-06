const assert = require('assert');

const utils = require('./test_utils.js');
const day01 = require('../day01.js');

describe('day01', function() {
    it('calc_fuel', function () {
        assert.equal(day01.calc_fuel('12'), 2);
        assert.equal(day01.calc_fuel('14'), 2);
        assert.equal(day01.calc_fuel('1969'), 654);
        assert.equal(day01.calc_fuel('100756'), 33583);
    });
    it('part1', function () {
        assert.equal(day01.part1(['12', '14', '1969']), 658);
        const masses = utils.get_input('day01');
        assert.equal(day01.part1(masses), 3282386);
    });
    it('calc_fuel_all', function () {
        assert.equal(day01.calc_fuel_all('12'), 2);
        assert.equal(day01.calc_fuel_all('14'), 2);
        assert.equal(day01.calc_fuel_all('1969'), 966);
        assert.equal(day01.calc_fuel_all('100756'), 50346);
    });
    it('part2', function () {
        assert.equal(day01.part2(['12', '14', '1969']), 970);
        const masses = utils.get_input('day01');
        assert.equal(day01.part2(masses), 4920708);
    });
});
