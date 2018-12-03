def day3_part2():
    occupied_spaces = {}
    overlapped = {}
    all_ids = []
    with open('input.txt') as file:
        for line in file:
            sizes = line.split(':')[1].strip().split('x')
            distances = line.split(':')[0].strip().split(',')
            from_left = int(distances[0].split('@')[1].strip())
            from_top = int(distances[1])
            id = int(distances[0].split('@')[0][1:])
            all_ids.append(id)
            for l in range(int(sizes[0])):
                for w in range(int(sizes[1])):
                    spot = (from_left+l, from_top+w)
                    if spot in occupied_spaces:
                        overlapped[occupied_spaces[spot]] = True
                        overlapped[id] = True
                    else:
                        occupied_spaces[spot] = id

    for i in range(len(all_ids)):
        if all_ids[i] not in overlapped:
            print(all_ids[i])


day3_part2()
