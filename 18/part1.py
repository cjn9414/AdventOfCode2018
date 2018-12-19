from helper import *


def day18_part1():
    lumber_area = []
    """ LOAD DATA INTO LIST FROM FILE """
    load_file('input.txt', lumber_area)

    """ RUN SIMULATION FOR TEN MINUTES """
    for minute in range(10):
        temp = lumber_area[:]
        change_lumber_area(temp, lumber_area)
    print(get_resource_value(lumber_area))


day18_part1()
