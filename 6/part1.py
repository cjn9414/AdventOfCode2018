def main():
    coords = {}
    with open('input.txt') as file:
        for line in file:
            pt = line.split(',')
            x = int(pt[0].strip())
            y = int(pt[1].strip())
            coords[(x, y)] = 0

    max_length = max(coords, key=lambda p: p[0])[0]
    max_height = max(coords, key=lambda p: p[1])[1]
    for y in range(0, max_height):
        for x in range(0, max_length):
            coord = get_smallest_coord(coords, (x, y))
            if coord is not None:
                if x == 0 or y == 0 or x == max_length-1 or y == max_height-1:
                    coords[coord] = -1
                else:
                    if coords[coord] != -1:
                        coords[coord] += 1

    print(coords[max(coords, key=lambda p:coords[p])])


def get_smallest_coord(coords, pt):
    shortest_length = None
    equal = True
    for coord in coords:
        d = abs(coord[0]-pt[0]) + abs(coord[1]-pt[1])
        if d == shortest_length:
            equal = True
        elif shortest_length is None or d < shortest_length:
            shortest_length = d
            closest_coord = coord
            equal = False
    if equal:
        return None
    else:
        return closest_coord


main()
