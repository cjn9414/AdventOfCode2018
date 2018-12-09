def main():
    with open('input.txt') as file:
        line = file.readline()
        line = line.split()
        sum, _ = helper(line)
        file.close()
    print(sum)


def helper(line):
    if len(line) == 0:
        return 0, 0
    sum = 0
    n_children = int(line[0])
    n_entries = int(line[1])
    jump = 2
    if n_children != 0:
        for i in range(n_children):
            next_sum, added_jump = helper(line[jump:])
            sum += next_sum
            jump += added_jump
    for i in range(0, n_entries):
        sum += int(line[i+jump])

    jump += n_entries
    return sum, jump


main()
