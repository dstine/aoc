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
    const range = input.split('-').map(Number);
    const start = range[0];
    const end = range[1];
    let count = 0;
    for (let n=start; n<=end; n++) {
        if (is_candidate(n)) {
            count += 1;
        }
    }
    return count;
}

function is_candidate(n, exactly_two) {
    const digits = n.toString().split('');
    const double_digits = [];
    let prior_prior_digit = -1;
    let prior_digit = digits[0];
    let i = 1;
    while (i < digits.length) {
        const curr_digit = digits[i];
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
