def day16_part2():
    function_holder = {}
    assigned = {}
    before, after, opcode = [], [], []
    test_lst = []
    testing(test_lst, 'input.txt')
    read_file(before, after, opcode, 'input.txt')
    for instruct in range(16):
        function_holder[instruct] = {}
        for j in range(16):
            function_holder[instruct][j] = 1
    for i in range(len(before)):
        after_ops, code = operations(before[i], after[i], opcode[i])
        for instruct in range(16):
            if function_holder[instruct][code]:
                if not after_ops[instruct]:
                    function_holder[instruct][code] = 0

    while len(function_holder) > 0:
        for func in function_holder:
            code = None
            if sum(function_holder[func].values()) == 1:
                for i in function_holder[func]:
                    if function_holder[func][i] == 1:
                        code = i
                        break
                if code is not None:
                    for j in function_holder:
                        del function_holder[j][code]
                    assigned[code] = func
                    break
        del function_holder[func]
    register = [0, 0, 0, 0]
    for instruction in test_lst:
        perform_instruction(instruction, assigned, register)
    print(register)


def perform_instruction(inst, opcodes, register):
    print(opcodes)
    op = opcodes[inst[0]]
    if op == 0:  # addr
        register[:] = register[:inst[3]] + [register[inst[1]] + register[inst[2]]] + register[inst[3]+1:]
    elif op == 1:
        register[:] = register[:inst[3]] + [register[inst[1]] + inst[2]] + register[inst[3]+1:]
    elif op == 2:
        register[:] = register[:inst[3]] + [register[inst[1]] * register[inst[2]]] + register[inst[3]+1:]
    elif op == 3:
        register[:] = register[:inst[3]] + [register[inst[1]] * inst[2]] + register[inst[3] + 1:]
    elif op == 4:
        register[:] = register[:inst[3]] + [register[inst[1]] & register[inst[2]]] + register[inst[3] + 1:]
    elif op == 5:
        register[:] = register[:inst[3]] + [register[inst[1]] & inst[2]] + register[inst[3] + 1:]
    elif op == 6:
        register[:] = register[:inst[3]] + [register[inst[1]] | register[inst[2]]] + register[inst[3] + 1:]
    elif op == 7:
        register[:] = register[:inst[3]] + [register[inst[1]] | inst[2]] + register[inst[3] + 1:]
    elif op == 8:
        register[:] = register[:inst[3]] + [register[inst[1]]] + register[inst[3] + 1:]
    elif op == 9:
        register[:] = register[:inst[3]] + [inst[1]] + register[inst[3] + 1:]
    elif op == 10:
        register[:] = register[:inst[3]] + [int(inst[1] > register[inst[2]])] + register[inst[3] + 1:]
    elif op == 11:
        register[:] = register[:inst[3]] + [int(register[inst[1]] > inst[2])] + register[inst[3] + 1:]
    elif op == 12:
        register[:] = register[:inst[3]] + [int(register[inst[1]] > register[inst[2]])] + register[inst[3] + 1:]
    elif op == 13:
        register[:] = register[:inst[3]] + [int(inst[1] == register[inst[2]])] + register[inst[3] + 1:]
    elif op == 14:
        register[:] = register[:inst[3]] + [int(register[inst[1]] == inst[2])] + register[inst[3] + 1:]
    else:
        register[:] = register[:inst[3]] + [int(register[inst[1]] == register[inst[2]])] + register[inst[3] + 1:]



def operations(before, after, opcode):
    after_ops = []
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] + before[opcode[2]]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] + opcode[2]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] * before[opcode[2]]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] * opcode[2]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] & before[opcode[2]]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] & opcode[2]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] | before[opcode[2]]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]] | opcode[2]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [before[opcode[1]]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [opcode[1]] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [int(opcode[1] > before[opcode[2]])] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [int(before[opcode[1]] > opcode[2])] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [int(before[opcode[1]] > before[opcode[2]])] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [int(opcode[1] == before[opcode[2]])] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [int(before[opcode[1]] == opcode[2])] + before[opcode[3]+1:])
    after_ops.append(before[:opcode[3]] + [int(before[opcode[1]] == before[opcode[2]])] + before[opcode[3]+1:])
    for i in range(len(after_ops)):
        after_ops[i] = int(after_ops[i] == after)
    return after_ops, opcode[0]


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


def testing(test_lst, fname):
    with open(fname) as file:
        past_line, line = '.', '.'
        while line != '' or past_line != '':
            past_line = line.strip()
            line = file.readline().strip()
        file.readline()
        for line in file:
            test_lst.append([int(i) for i in line.strip().split()])
    file.close()


day16_part2()
