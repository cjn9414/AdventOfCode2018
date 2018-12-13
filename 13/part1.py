from cart import Cart


def init(carts, tracks):
    """ INITIALIZE CART AND TRACK LISTS """
    for y in range(len(tracks)):
        track = tracks[y]
        for x in range(len(track)):
            ch = track[x]
            if ch in '<>^v':
                carts.append(Cart(x, y, ch))


def day13_part1():
    carts = []
    tracks = []
    collision = False

    with open('input.txt') as file:
        for line in file:
            tracks.append(line.strip('\n'))
        file.close()

    init(carts, tracks)

    """ LOOP UNTIL FIRST COLLISION FOUND """
    while not collision:
        for cart in carts:
            cart.update(tracks)
            if cart.had_collision():
                print(cart.x, cart.y, sep=',')
                collision = True
        carts.sort(key=lambda c: int(str(c.y+c.x)))


day13_part1()
