def day16_part1():
    before, after, opcode = [], [], []
    read_file(before, after, opcode, 'input.txt')
    count = 0
    for i in range(len(before)):
        like_codes = 0
        like_codes += adding(before[i], after[i], opcode[i])
        like_codes += mult(before[i], after[i], opcode[i])
        like_codes += bitwise_and(before[i], after[i], opcode[i])
        like_codes += bitwise_or(before[i], after[i], opcode[i])
        like_codes += setting(before[i], after[i], opcode[i])
        like_codes += greater_than(before[i], after[i], opcode[i])
        like_codes += equalities(before[i], after[i], opcode[i])
        if like_codes >= 3:
            count += 1
    print(count)


def adding(before, after, opcode):
    addition_reg = before[:opcode[3]] + [before[opcode[1]] + before[opcode[2]]] + before[opcode[3]+1:]
    addition_im = before[:opcode[3]] + [before[opcode[1]] + opcode[2]] + before[opcode[3]+1:]
    return int(addition_reg == after) + int(addition_im == after)


def mult(before, after, opcode):
    mult_reg = before[:opcode[3]] + [before[opcode[1]] * before[opcode[2]]] + before[opcode[3]+1:]
    mult_im = before[:opcode[3]] + [before[opcode[1]] * opcode[2]] + before[opcode[3]+1:]
    return int(mult_reg == after) + int(mult_im == after)


def bitwise_and(before, after, opcode):
    bitwise_reg = before[:opcode[3]] + [before[opcode[1]] & before[opcode[2]]] + before[opcode[3]+1:]
    bitwise_im = before[:opcode[3]] + [before[opcode[1]] & opcode[2]] + before[opcode[3]+1:]
    return int(bitwise_reg == after) + int(bitwise_im == after)


def bitwise_or(before, after, opcode):
    bitwise_reg = before[:opcode[3]] + [before[opcode[1]] | before[opcode[2]]] + before[opcode[3]+1:]
    bitwise_im = before[:opcode[3]] + [before[opcode[1]] | opcode[2]] + before[opcode[3]+1:]
    return int(bitwise_reg == after) + int(bitwise_im == after)


def setting(before, after, opcode):
    before_reg = before[:opcode[3]] + [before[opcode[1]]] + before[opcode[3]+1:]
    before_im = before[:opcode[3]] + [opcode[1]] + before[opcode[3]+1:]
    return int(before_reg == after) + int(before_im == after)


def greater_than(before, after, opcode):
    gtir = before[:opcode[3]] + [int(opcode[1] > before[opcode[2]])] + before[opcode[3]+1:]
    gtri = before[:opcode[3]] + [int(before[opcode[1]] > opcode[2])] + before[opcode[3]+1:]
    gtrr = before[:opcode[3]] + [int(before[opcode[1]] > before[opcode[2]])] + before[opcode[3]+1:]
    return int(gtir == after) + int(gtri == after) + int(gtrr == after)


def equalities(before, after, opcode):
    eqir = before[:opcode[3]] + [int(opcode[1] == before[opcode[2]])] + before[opcode[3]+1:]
    eqri = before[:opcode[3]] + [int(before[opcode[1]] == opcode[2])] + before[opcode[3]+1:]
    eqrr = before[:opcode[3]] + [int(before[opcode[1]] == before[opcode[2]])] + before[opcode[3]+1:]
    return int(eqir == after) + int(eqri == after) + int(eqrr == after)


def read_file(before, after, opcode, fname):
    with open(fname) as file:
        end = False
        for line in file:
            line = line.strip()
            if line == '':
                if end:
                    break
                else:
                    end = True
            else:
                end = False
                line = line.split(' ', 1)
                if line[0] == 'Before:' or line[0] == "After:":
                    vals = line[1].strip(' [').strip(']').split(',')
                    vals = [int(vals[i]) for i in range(len(vals))]
                    if line[0] == 'Before:':
                        before.append(vals)
                    else:
                        after.append(vals)
                else:
                    split = line[1].split()
                    vals = [line[0]] + split
                    opcode.append([int(vals[i].strip()) for i in range(len(vals))])
    file.close()


day16_part1()

