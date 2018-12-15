def day14_part1():
    num_recipes = input()
    recipe_scores = [3, 7]
    elves = [0, 1]
    while len(recipe_scores) < num_recipes + 10:
        score = 0
        for elf in elves:
            score += recipe_scores[elf]
        for dig in str(score):
            recipe_scores.append(int(dig))
        for i in range(len(elves)):
            elves[i] = (elves[i] + 1 + recipe_scores[elves[i]]) % len(recipe_scores)
    result = recipe_scores[num_recipes:num_recipes+11]
    for score in result:
        print(score, end='')


day14_part1()
