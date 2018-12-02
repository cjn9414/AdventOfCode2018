def main():
    with open('input.txt') as file:
        ids = set()
        for line in file:
            line = line.strip()
            for set_id in ids:
                for idx_slice in range(len(line)-1):
                    sliced_line = line[0:idx_slice] + line[idx_slice+1:]
                    sliced_id = set_id[0:idx_slice] + set_id[idx_slice+1:]
                    slice_difference = difference(sliced_id, sliced_line)
                    if slice_difference == 0:
                        print(sliced_line)
                        break
                    elif slice_difference >= 2:
                        break
            ids.add(line.strip())


def difference(st1, st2):
    diff = 0
    for idx in range(len(st2)):
        if st1[idx] != st2[idx]:
            diff += 1
        if diff >= 2:
            break
        idx += 1
    return diff


main()