def main_5():
    with open('input.txt') as file:
            polymer = file.readline().strip()
    reacting = True
    while reacting:
        reacting = False
        for i in range(len(polymer)-1):
            try:
                if polymer[i].lower() == polymer[i+1].lower():
                    if polymer[i] != polymer[i+1]:
                        polymer = polymer[0:i] + polymer[i+2:]
                        reacting = True
            except IndexError:
                break
    print(len(polymer))


main_5()
