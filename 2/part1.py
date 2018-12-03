def day2_part1():
    two_count = 0
    three_count = 0
    with open('input.txt') as file:
        for line in file:
            two_bust = False
            three_bust = False
            letters = {}
            for character in line:
                if character in letters:
                    letters[character] += 1
                else:
                    letters[character] = 1
            for letter in letters:
                if letters[letter] == 2 and not two_bust:
                    two_count += 1
                    two_bust = True
                elif letters[letter] == 3 and not three_bust:
                    three_count += 1
                    three_bust = True
    print(two_count*three_count)


day2_part1()
