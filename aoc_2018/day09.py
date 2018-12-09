def part1(n_players, last_marble):
    circle = [0]
    scores = [0] * n_players
    current_marble = 0
    current_index = 0
    current_player = 0
    while True:
        #print('[{}] {:2d} : {}'.format(current_player, current_index, circle))
        current_marble += 1
        current_player = (current_player + 1) % n_players
        
        if (current_marble % 23 == 0):
            current_index -= 7
            if current_index < 0:
                current_index += len(circle)
            removed_marble = circle.pop(current_index)
            score = current_marble + removed_marble
            scores[current_player] += score
        else:
            current_index += 2
            if current_index > len(circle):
                current_index -= len(circle)
            circle.insert(current_index, current_marble)

        if current_marble > last_marble:
            break

    return max(scores)
