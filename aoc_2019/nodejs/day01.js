module.exports.calc_fuel = calc_fuel;
module.exports.part1 = part1;
module.exports.calc_fuel_all = calc_fuel_all;
module.exports.part2 = part2;

function calc_fuel(mass) {
    var fuel = Math.floor(mass/3) - 2;
    return fuel < 0? 0 : fuel;
}

function part1(masses) {
    return masses.map(calc_fuel).reduce((x, y) => x+y, 0);
}

function calc_fuel_all(mass) {
    var total = 0;
    var current = mass;
    while (current > 0) {
        current = calc_fuel(current);
        total += current;
    }
    return total;
}

function part2(masses) {
    return masses.map(calc_fuel_all).reduce((x, y) => x+y, 0);
}
