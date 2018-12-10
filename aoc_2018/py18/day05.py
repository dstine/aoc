import sys

def part1(polymer):
    return len(react(polymer))

def part2(polymer):
    letters = {ch.lower() for ch in polymer}
    least = sys.maxsize
    for letter in  letters:
        other_letters = [ch for ch in polymer if ch.lower() != letter]
        cleaned = ''.join(other_letters)
        reacted = react(cleaned)
        if len(reacted) < least:
            least = len(reacted)
    return least

# recursive approach blew the stack
def react(polymer):
    # pre-compute information about each character for performance
    # for my puzzle input, reduced runtime by about 60%
    polymer = [(ch, ch.lower(), ch.islower()) for ch in polymer]
    prior = ''
    reacted = polymer
    while prior != reacted:
        prior = reacted
        reacted = react_once(prior)
    # extract just the string to return the result
    reacted_polymer = ''.join([c[0] for c in reacted])
    return reacted_polymer

def react_once(polymer):
    out = []
    i = 0
    last_index = len(polymer)-1

    while i < last_index:
        c1 = polymer[i]
        c2 = polymer[i+1]
        same_letter = c1[1] == c2[1]    # lower()
        different_case = c1[2] != c2[2] # islower()
        if same_letter and different_case:
            # reaction
            i += 2
        else:
            # no reaction
            out.append(polymer[i])
            i += 1
        if i == last_index:
            out.append(polymer[i])

    return out

# used for profiling:
#     python3 -m cProfile day05.py
if __name__ == '__main__':

    # duplicated from test file
    def get_my_input():
        path = 'data/day05_input.txt'
        return get_one_liner(path)

    def get_one_liner(path):
        with open(path) as file:
            # only one line in file
            for line in file:
                return line.rstrip()

    part2('dabAcCaCBAcCcaDA')
    part2(get_my_input())
