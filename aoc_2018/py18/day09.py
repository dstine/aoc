from collections import deque

def part1(n_players, last_marble):
    return compute(n_players, last_marble)

def part2(n_players, last_marble):
    return compute(n_players, last_marble)

def compute(n_players, last_marble):
    circle = deque([0])
    scores = [0] * n_players
    for marble in range(1, last_marble+1):
        if marble % 23 == 0:
            circle.rotate(7)
            removed_marble = circle.pop()
            score = marble + removed_marble
            player = (marble % n_players) - 1
            scores[player] += score
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)
