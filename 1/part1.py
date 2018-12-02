def main():
    frequency = 0
    with open('input.txt') as file:
        for line in file:
            frequency += int(line)
    print(frequency)


main()
