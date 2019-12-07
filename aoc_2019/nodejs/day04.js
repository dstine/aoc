module.exports = {
    is_candidate1,
    part1,
    is_candidate2,
    part2,
};

function is_candidate1(n) {
    return is_candidate(n, false);
}

function part1(input) {
    return part(input, is_candidate1);
}

function is_candidate2(n) {
    return is_candidate(n, true);
}

function part2(input) {
    return part(input, is_candidate2);
}

function part(input, is_candidate) {
    var range = input.split('-').map(Number);
    var start = range[0];
    var end = range[1];
    var count = 0;
    for (var n=start; n<=end; n++) {
        if (is_candidate(n)) {
            count += 1;
        }
    }
    return count;
}

function is_candidate(n, exactly_two) {
    var digits = n.toString().split('');
    var double_digits = [];
    var prior_prior_digit = -1;
    var prior_digit = digits[0];
    var i = 1;
    while (i < digits.length) {
        var curr_digit = digits[i];
        // Two adjacent digits are the same (like 22 in 122345).
        // AND if "exactly_two", are not part of a larger group of matching digits
        if (curr_digit == prior_digit) {
            if (!exactly_two || (i < 2) || (prior_digit != prior_prior_digit)) {
                double_digits.push(curr_digit);
            } else if (double_digits.includes(curr_digit)) {
                double_digits.pop();
            }
        }
        // Going from left to right, the digits never decrease;
        // they only ever increase or stay the same (like 111123 or 135679).
        if (curr_digit < prior_digit) {
            return false;
        }
        prior_prior_digit = prior_digit;
        prior_digit = curr_digit;
        i += 1;
    }
    return double_digits.length > 0;
}
