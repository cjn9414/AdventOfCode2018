def day7_part1():
    ordering = {}
    order = ""

    """ CREATE DATA STRUCTURE FOR STEP ORDERING"""
    with open('input.txt') as file:
        count = 0
        for line in file:
            count += 1
            lst = [line[i] for i in range(len(line)) if line[i].isupper()]
            lst = lst[1:]
            if lst[0] not in ordering:
                ordering[lst[0]] = set()
            if lst[1] not in ordering:
                ordering[lst[1]] = set()
            ordering[lst[1]].add(lst[0])
        file.close()

    """ DETERMINE ORDER THAT STEPS NEED TO BE TAKEN """
    while len(ordering) > 0:
        removed = ""
        next = ''
        for ent in ordering:
            if len(ordering[ent]) == 0:
                next += ent
                removed += ent
        next = ''.join(sorted(removed))
        order += next[0]
        removed = next[0]
        for ent in ordering:
            if removed in ordering[ent]:
                ordering[ent].remove(removed)
        del ordering[removed]
    print(order)


day7_part1()
