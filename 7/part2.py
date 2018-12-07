def day7_part2():
    ordering = {}
    order = ""
    total_time = 0
    workers = [['', -1] for _ in range(5)]

    """ CREATE DATA STRUCTURE FOR STEP ORDERING"""
    with open('input.txt') as file:
        for line in file:
            lst = [line[i] for i in range(len(line)) if line[i].isupper()]
            lst = lst[1:]
            if lst[0] not in ordering:
                ordering[lst[0]] = set()
            if lst[1] not in ordering:
                ordering[lst[1]] = set()
            ordering[lst[1]].add(lst[0])
        file.close()

    """ DETERMINE ORDERING AND TIME TAKEN """
    working = True
    while len(ordering) > 0 or working:
        working = False
        removed = ""
        next = ''

        """ FIND ALL STEPS WITH NO PREREQUISITES """
        for ent in ordering:
            if len(ordering[ent]) == 0:
                next += ent
                removed += ent
        next = ''.join(sorted(removed))

        """ ASSIGN WORKERS TO NEXT STEPS """
        for worker in workers:
            if len(next) == 0:
                break
            if worker[1] <= 0:
                worker[0] = next[0]
                worker[1] = ord(next[0])-4
                del ordering[next[0]]
                next = next[1:]

        """ INCREMENT TOTAL TIME AND WORK TIME FOR EACH WORKER """
        for worker in workers:
            worker[1] -= 1
            if worker[1] == 0:
                order += worker[0]
                for ent in ordering:
                    if worker[0] in ordering[ent]:
                        ordering[ent].remove(worker[0])
            elif worker[1] > 0:
                working = True
        total_time += 1

    print(total_time)


day7_part2()
