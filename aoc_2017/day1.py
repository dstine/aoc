def day1(digits, step):
    ndigits = len(digits)
    sum = 0
    for idx in range(0, ndigits):
        digit = digits[idx]
        partner = digits[(idx + step) % ndigits]
        if digit == partner:
            sum += int(digit)
    return sum

def day1_1(digits):
    return day1(digits, 1)

def day1_2(digits):
    step = len(digits) // 2
    return day1(digits, step)
