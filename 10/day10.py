def day10():

    positions = []
    velocities = []

    """ LOAD DATA FROM FILE """
    with open('input.txt') as file:
        for line in file:
            line = line.split('<')
            p = line[1]
            v = line[2]
            px = int(p.split(',')[0].strip())
            py = int(p.split(',')[1].split('>')[0].strip())
            vx = int(v.split(',')[0].strip())
            vy = int(v.split(',')[1].split('>')[0].strip())
            positions.append([px, py])
            velocities.append([vx, vy])
        file.close()
    seconds = 0

    """ FIND MESSAGE WHEN STARS ALL ALL NEARBY EACH OTHER """
    aligned = False
    while not aligned:
        aligned = True
        for i in range(len(positions)):
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
        for pos in positions:
            all_nearby = False
            for other in positions:
                if pos != other:
                    if abs(pos[0]-other[0]) + abs(pos[1]-other[1]) <= 2:
                        all_nearby = True
                        break
            if not all_nearby:
                aligned = False
                break
        seconds += 1

    """ PRINT OUT MESSAGE """
    for y in range(min(pos[1] for pos in positions), max(pos[1] for pos in positions)+1):
        for x in range(min(pos[0] for pos in positions), max(pos[0] for pos in positions)+1):
            if [x, y] in positions:
                print('*', end='')
            else:
                print('.', end='')
        print('')
    print(seconds)


day10()