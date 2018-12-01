# find total for one pass
def part1(changes):
    result = 0
    for change in changes:
        result += int(change)
    return result

# find first repeated intermediate result for any number of passes
def part2(changes):
    result = 0
    results = { result }
    while True:
        for change in changes:
            result += int(change)
            if result in results:
                return result
            results.add(result)
