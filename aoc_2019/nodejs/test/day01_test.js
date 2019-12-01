var assert = require('assert');

var day01 = require('../day01.js')

describe('day01', function() {
    it('calc_fuel', function () {
        assert.equal(day01.calc_fuel('12'), 2);
        assert.equal(day01.calc_fuel('14'), 2);
        assert.equal(day01.calc_fuel('1969'), 654);
        assert.equal(day01.calc_fuel('100756'), 33583);
    });
});

describe('day01', function() {
    it('part1', function () {
        assert.equal(day01.part1(['12', '14', '1969']), 658);
        var masses = get_input();
        assert.equal(day01.part1(masses), 3282386);
    });
});

describe('day01', function() {
    it('calc_fuel_all', function () {
        assert.equal(day01.calc_fuel_all('12'), 2);
        assert.equal(day01.calc_fuel_all('14'), 2);
        assert.equal(day01.calc_fuel_all('1969'), 966);
        assert.equal(day01.calc_fuel_all('100756'), 50346);
    });
});

describe('day01', function() {
    it('part2', function () {
        assert.equal(day01.part2(['12', '14', '1969']), 970);
        var masses = get_input();
        assert.equal(day01.part2(masses), 4920708);
    });
});

var fs = require('fs');
var path = require('path');

function get_input() {
    var input_path = path.join(__dirname, '../../data/day01_input.txt');
    var input = fs.readFileSync(input_path, 'utf-8');
    var lines = input.split('\n');
    return lines;
}
