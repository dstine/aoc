module.exports = {
    is_candidate,
    part1,
};

function is_candidate(n) {
    var digits = n.toString().split('');
    var has_double = false;
    for (var i=0; i<digits.length-1; i++) {
        // Two adjacent digits are the same (like 22 in 122345).
        if (!has_double && (digits[i] == digits[i+1])) {
            has_double = true;
        }
        // Going from left to right, the digits never decrease;
        // they only ever increase or stay the same (like 111123 or 135679).
        if (digits[i] > digits[i+1]) {
            return false;
        }
    }
    return has_double;
}

function part1(input) {
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
