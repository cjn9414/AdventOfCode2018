def day1_part2():
    already_hit = set()
    frequency = 0
    already_hit.add(frequency)
    found = False
    while not found:
        with open('input.txt') as file:
            for line in file:
                frequency += int(line)
                if frequency in already_hit:
                    print(frequency)
                    found = True
                    break
                else:
                    already_hit.add(frequency)


day1_part2()
