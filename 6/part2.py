def main():
    coords = {}
    area = 0
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
            if coord:
                area += 1
    print(area)


def get_smallest_coord(coords, pt):
    total_dist = 0
    for coord in coords:
        total_dist += abs(coord[0]-pt[0]) + abs(coord[1]-pt[1])
    if total_dist >= 10000:
        return False
    else:
        return True


main()