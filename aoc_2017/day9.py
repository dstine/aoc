GROUP_OPEN = '{'
GROUP_CLOSE = '}'
GARBAGE_OPEN = '<'
GARBAGE_CLOSE = '>'
IGNORE = '!'

def day9_1(input):
    chars = list(input)
    return score(chars)

def score(chars):
    nesting_level = -1
    in_garbage = False
    score = 0
    while len(chars) > 0:
        char = chars.pop(0)
        if IGNORE == char:
            chars.pop(0)
        elif GARBAGE_OPEN == char and not in_garbage:
            in_garbage = True
        elif GARBAGE_CLOSE == char and in_garbage:
            in_garbage = False
        elif in_garbage:
            continue
        elif GROUP_OPEN == char:
            nesting_level += 1
        elif GROUP_CLOSE == char:
            score += 1 + nesting_level
            nesting_level -= 1
    return score
