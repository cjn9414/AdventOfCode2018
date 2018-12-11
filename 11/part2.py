serial = int(input())


def main():
    max_pwr, chances = 0, 0
    max_x, max_y, max_size = None, None, None
    max_pwr_changed = True
    """ FINDS MAX POWER FOR EVERY SQUARE SIZE """
    while max_pwr_changed:  # assuming if max doesn't change after increasing
        chances += 1        # square size, it will never change
        max_pwr_changed = False
        for y in range(0, 300):
            for x in range(0, 300):
                total_pwr, size = largest_square_at_corner(x, y, -100, 1, chances, 0)
                if total_pwr > max_pwr:
                    max_pwr = total_pwr
                    max_x = x
                    max_y = y
                    max_size = size
                    max_pwr_changed = True
    print(max_x, max_y, max_size, sep=',')


def largest_square_at_corner(x, y, past_pwr, size, chances, prev_size):
    """ FIND THE MAXIMUM POWER POSSIBLE AT A GIVEN CORNER CELL """
    total_pwr = 0
    if x + size > 300 or y + size > 300 or chances == 0:
        return past_pwr, prev_size
    for xi in range(x, x + size):
        for yi in range(y, y + size):
            total_pwr += get_pwr(xi, yi)
    if total_pwr >= past_pwr:
        return largest_square_at_corner(x, y, total_pwr, size+1, chances, size)
    else:
        return largest_square_at_corner(x, y, past_pwr, size+1, chances-1, prev_size)


def get_pwr(x, y):
    """ FINDS THE POWER AT A GIVEN CELL """
    global serial
    rack_id = x + 10
    pwr = rack_id * y
    pwr += serial
    pwr *= rack_id
    if pwr < 100:
        pwr = 0
    else:
        pwr = int(str(pwr)[-3])
    pwr -= 5
    return pwr


main()
