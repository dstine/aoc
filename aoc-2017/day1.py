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

print("Day 1, Problem 1")
print(day1_1("1122"))
print(day1_1("1111"))
print(day1_1("1234"))
print(day1_1("91212129"))

def day1_2(digits):
    step = len(digits) // 2
    return day1(digits, step)

print("Day 1, Problem 2")
print(day1_2("1212"))
print(day1_2("1221"))
print(day1_2("123425"))
print(day1_2("123123"))
print(day1_2("12131415"))
