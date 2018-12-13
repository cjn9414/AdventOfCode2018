from cart import Cart


def init(carts, tracks):
    """ INITIALIZE CART AND TRACK LISTS """
    for y in range(len(tracks)):
        track = tracks[y]
        for x in range(len(track)):
            ch = track[x]
            if ch in '<>^v':
                carts.append(Cart(x, y, ch))


def day13_part2():
    carts = []
    tracks = []

    with open('input.txt') as file:
        for line in file:
            tracks.append(line.strip('\n'))
        file.close()

    init(carts, tracks)
    """ LOOP UNTIL THERE IS ONLY ONE CART LEFT """
    while len(carts) > 1:
        to_remove = []
        for cart in carts:
            if not cart.crashed:  # if it has crashed, leave it
                cart.update(tracks)
                if cart.had_collision():  # find two carts that crashed
                    cart.fix_tracks(tracks)
                    cart.crashed = True
                    (x, y) = (cart.x, cart.y)
                    to_remove.append(cart)
                    for other in carts:
                        if cart != other:
                            if other.x == x and other.y == y:
                                to_remove.append(other)
                                other.fix_tracks(tracks)
                                other.crashed = True
        for cart in to_remove:  # remove carts that crashed from list
            carts.remove(cart)
        carts.sort(key=lambda c: int(str(c.y+c.x)))  # resort carts

    for cart in carts:
        print(cart.x, cart.y, sep=',')


day13_part2()
