import re

with open("2023/02/input.txt") as input_file:
    input = input_file.read().splitlines()


colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# part 1

ok_lines = []
sum_games = 0

for line in input:
    game_number = int(re.findall("Game (\d+)", line)[0])
    line_match = False
    for color in colors:
        matches = re.findall("((\d+) " + color + ")", line)

        for match in matches:
            if int(match[1]) > colors[color]:
                line_match = True

    if not line_match:
        sum_games += game_number

print("result for part one is: " + str(sum_games))

# part 2

cubes_mulitplied = []
for line in input:
    game_number = int(re.findall("Game (\d+)", line)[0])
    color_match = []
    for color in colors:
        matches = re.findall("((\d+) " + color + ")", line)

        new_matches = []
        for match in matches:
            new_matches.append(int(match[1]))

        new_matches.sort()
        color_match.append(new_matches[-1])

    cubes_mulitplied.append(color_match[0] * color_match[1] * color_match[2])


print("result for part two is: " + str(sum(cubes_mulitplied)))
