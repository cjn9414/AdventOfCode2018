
def get_resource_value(lumber_area):
    trees, lumber_yards = 0, 0
    for row in lumber_area:
        for acre in row:
            if acre == '|':
                trees += 1
            elif acre == '#':
                lumber_yards += 1
    return lumber_yards*trees


def change_lumber_area(read_from, write_to):
    for y in range(1, len(read_from)-1):
        for x in range(1, len(read_from[y])-1):
            trees, lumberyards = 0, 0
            local = []
            local.append(read_from[y][x-1])
            local.append(read_from[y][x+1])
            local.append(read_from[y+1][x-1])
            local.append(read_from[y-1][x-1])
            local.append(read_from[y+1][x+1])
            local.append(read_from[y-1][x+1])
            local.append(read_from[y-1][x])
            local.append(read_from[y+1][x])
            for acre in local:
                if acre == '|':
                    trees += 1
                elif acre == '#':
                    lumberyards += 1
            if write_to[y][x] == '.':
                if trees >= 3:
                    write_to[y] = write_to[y][0:x] + '|' + write_to[y][x+1:]
            elif write_to[y][x] == '|':
                if lumberyards >= 3:
                    write_to[y] = write_to[y][0:x] + '#' + write_to[y][x+1:]
            elif read_from[y][x] == '#':
                if trees == 0 or lumberyards == 0:
                    write_to[y] = write_to[y][0:x] + '.' + write_to[y][x+1:]


def load_file(fname, lumber_area):
    with open(fname) as file:
        first_line = file.readline().strip()
        lumber_area.append('@' * (len(first_line)+2))  # surround area with '@'
        lumber_area.append('@' + first_line + '@')     # to avoid index errors
        for line in file:
            lumber_area.append('@' + line.strip() + '@')
        lumber_area.append('@' * (len(first_line) + 2))
        file.close()