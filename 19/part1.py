def day19_part1():
    program = []
    registers = [0, 0, 0, 0, 0, 0]
    ip = 1
    with open('input.txt') as file:
        file.readline()
        for line in file:
            line = line.strip().split()
            program.append(line)
    while True:
        instr = program[registers[ip]]
        func = instr[0] + '(' + instr[1] + ',' + instr[2] + ',' + instr[3] + ',registers' + ')'
        exec(func)
        registers[ip] += 1
        if registers[ip] >= len(program):
            break
    print(registers)


def addr(first, second, into, reg):
    reg[into] = reg[first] + reg[second]


def addi(first, second, into, reg):
    reg[into] = reg[first] + second


def mulr(first, second, into, reg):
    reg[into] = reg[first] * reg[second]


def muli(first, second, into, reg):
    reg[into] = reg[first] * second


def setr(first, second, into, reg):
    reg[into] = reg[first]


def seti(first, second, into, reg):
    reg[into] = first


def gtrr(first, second, into, reg):
    reg[into] = int(reg[first] > reg[second])


def eqrr(first, second, into, reg):
    reg[into] = int(reg[first] == reg[second])


day19_part1()
