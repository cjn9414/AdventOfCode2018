def day12_part1():
    sequences = {}
    generations = 20
    """ LOAD DATA INTO DICTIONARY FROM FILE """
    with open('input.txt') as file:
        inp = '....' + file.readline().split(':')[1].strip()
        for line in file:
            line = line.split('=>')
            if len(line[0].strip()) > 0:
                sequences[line[0].strip()] = line[1].strip()
        file.close()

    """ PERFORM NEXT GENERATION """
    for gen in range(generations):
        next_gen = ".."
        for i in range(2, len(inp)-2):
            key = inp[i-2:i+3]
            next_gen += sequences[key]
        inp = next_gen.rstrip(',') + '....'

    """ CALCULATE TOTAL FROM POTS CONTAINING PLANTS """
    total = 0
    for i in range(0, len(inp)):
        if inp[i] == '#':
            total += i-4
    print(total)


day12_part1()
