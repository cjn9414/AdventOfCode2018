def day14_part2():
    seq = input()
    recipe_scores = "37"
    elf1, elf2 = 0, 1
    while seq not in recipe_scores[-len(seq)-1:]:
        recipe_scores += str(int(recipe_scores[elf1]) + int(recipe_scores[elf2]))
        elf1 = (1 + elf1 + int(recipe_scores[elf1])) % len(recipe_scores)
        elf2 = (1 + elf2 + int(recipe_scores[elf2])) % len(recipe_scores)
    if recipe_scores[len(seq)] == seq:
        print(len(recipe_scores)-len(seq))
    else:
        print(len(recipe_scores)-len(seq)-1)


day14_part2()
