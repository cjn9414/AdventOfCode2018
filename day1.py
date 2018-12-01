def main():
    already_hit = set()
    count = 0
    already_hit.add(count)
    found = False
    while not found:
        with open('input.txt') as file:
            for line in file:
                count += int(line)
                if count in already_hit:
                    print(count)
                    found = True
                    break
                else:
                    already_hit.add(count)
    print(already_hit)


main()
