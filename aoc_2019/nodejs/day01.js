module.exports = {
    calc_fuel,
    calc_fuel_all,
    part1,
    part2,
};

function calc_fuel(mass) {
    const fuel = Math.floor(mass/3) - 2;
    return Math.max(0, fuel);
}

function part1(masses) {
    return masses.map(calc_fuel).reduce((x, y) => x+y, 0);
}

function calc_fuel_all(mass) {
    let total = 0;
    let current = mass;
    while (current > 0) {
        current = calc_fuel(current);
        total += current;
    }
    return total;
}

function part2(masses) {
    return masses.map(calc_fuel_all).reduce((x, y) => x+y, 0);
}
