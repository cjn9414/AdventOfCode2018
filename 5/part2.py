def main():
    lengths = {}
    letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    with open('input.txt') as file:
            old_polymer = file.readline().strip()
    for ch in letters:
        print(ch)
        change = True
        polymer = old_polymer.replace(ch, '')
        polymer = polymer.replace(ch.upper(), '')
        while change:
            change = False
            for i in range(len(polymer)-1):
                try:
                    if polymer[i].lower() == polymer[i+1].lower():
                        if polymer[i] != polymer[i+1]:
                            polymer = polymer[0:i] + polymer[i+2:]
                            change = True
                except IndexError:
                    break
        lengths[ch] = len(polymer)
    smallest_poly_length = min(lengths.keys(), key=lambda key: lengths[key])
    print(smallest_poly_length, lengths[smallest_poly_length])


main()
