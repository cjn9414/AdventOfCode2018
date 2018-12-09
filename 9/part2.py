class Node:
    def __init__(self, val, ccw, cw):
        self.ccw = ccw
        self. cw = cw
        self.val = val


def main():
    n_players = 400
    player_scores = [0 for _ in range(n_players)]
    curr_marble, marble_number = get_first_marbles()
    last_marble = 7186400
    while marble_number <= last_marble:
        if marble_number % 23 == 0:
            player_scores[marble_number % n_players] += marble_number
            for _ in range(7):
                curr_marble = curr_marble.ccw
            player_scores[marble_number % n_players] += curr_marble.val
            curr_marble.ccw.cw = curr_marble.cw
            curr_marble.cw.ccw = curr_marble.ccw
            curr_marble = curr_marble.cw
        else:
            curr_marble = curr_marble.cw
            new_marble = Node(marble_number, curr_marble, curr_marble.cw)
            curr_marble.cw = new_marble
            curr_marble = new_marble
            curr_marble.cw.ccw = curr_marble
        marble_number += 1
    print(max(player_scores))


def get_first_marbles():
    first = Node(0, None, None)
    second = Node(1, None, None)
    third = Node(2, first, second)
    first.cw = third
    first.ccw = second
    second.cw = first
    second.ccw = third
    return third, 3


main()
