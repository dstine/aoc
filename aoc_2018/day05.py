def part1(polymer):
    return len(react(polymer))

def react(polymer):
    input = polymer
    out = []
    i = 0
    last_index = len(polymer)-1

    while i < last_index:
        c1 = polymer[i]
        c2 = polymer[i+1]
        same_letter = c1.lower() == c2.lower()
        different_case = c1.islower() != c2.islower()
        if same_letter and different_case:
            # reaction
            i += 2
        else:
            # no reaction
            out += c1
            i += 1
        if i == last_index:
            out += polymer[i]

    output = ''.join(out)
    if input == output:
        return output
    else:
        return react(output)
