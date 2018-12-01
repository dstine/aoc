import operator

operators = {
    '+': operator.add, 
    '-': operator.sub,
    }

def compute(change, result):
    sign = change[0]
    val = int(change[1:])
    return operators[sign](result, val)

# find total for one pass
def part1(changes):
    result = 0
    for change in changes:
        result = compute(change, result)
    return result

# find first repeated intermediate result for any number of passes
def part2(changes):
    result = 0
    results = { result }
    while True:
        for change in changes:
            result = compute(change, result)
            if result in results:
                return result
            results.add(result)
