def day1_part1():
    frequency = 0
    with open('input.txt') as file:
        for line in file:
            frequency += int(line)
    print(frequency)


day1_part1()
