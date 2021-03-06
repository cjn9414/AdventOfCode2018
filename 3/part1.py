def day3_part1():
    double_occupied = {}
    overlap_count = 0
    with open('input.txt') as file:
        for line in file:
            sizes = line.split(':')[1].strip().split('x')
            distances = line.split(':')[0].strip().split(',')
            from_left = int(distances[0].split('@')[1].strip())
            from_top = int(distances[1])
            for l in range(int(sizes[0])):
                for w in range(int(sizes[1])):
                    fabric = (from_left+l, from_top+w)
                    if fabric in double_occupied:
                        if not double_occupied[fabric]:
                            overlap_count += 1
                        double_occupied[fabric] = True

                    else:
                        double_occupied[fabric] = False
    print(overlap_count)


day3_part1()

