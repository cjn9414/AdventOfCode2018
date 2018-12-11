serial = int(input())


def main():
    max_pwr = 0
    max_x = None
    max_y = None
    square_sz = 3
    grid_sz = 300
    """ FIND MAX POWER FOR SQUARE SIZE OF THREE """
    for y in range(0, grid_sz-square_sz+1):
        for x in range(0, grid_sz-square_sz+1):
            total_pwr = 0
            for xi in range(x, x+square_sz):
                for yi in range(y, y+square_sz):
                    total_pwr += get_pwr(xi, yi)
            if total_pwr > max_pwr:
                max_pwr = total_pwr
                max_x = x
                max_y = y
    print(max_x, max_y, sep=',')


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
