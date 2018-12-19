from helper import *


def day18_part2():
    lumber_area, past = [], []

    """ LOAD DATA INTO LIST FROM FILE """
    load_file('input.txt', lumber_area)

    """ FIND WHEN PATTERN REPEATS """
    minute = 0
    while True:
        temp = lumber_area[:]
        change_lumber_area(temp, lumber_area)
        minute += 1
        if lumber_area in past:
            break
        if len(past) == 100:
            past.pop(0)
        temp = lumber_area[:]
        past.append(temp)

    """ CALCULATE PERIOD OF PATTERN REPETITION """
    period = 1
    for i in range(len(past)-1, -1, -1):
        if past[i] == lumber_area:
            break
        period += 1

    """ FAST FORWARD IN TIME """
    remaining = (1000000000-minute) % period
    for _ in range(remaining):
        temp = lumber_area[:]
        change_lumber_area(temp, lumber_area)
    print(get_resource_value(lumber_area))


day18_part2()