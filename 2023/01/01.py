import re

with open("2023/01/input.txt") as input_file:
    input = input_file.read().splitlines()

# part one

numbers = []

for line in input:
    for character in line:
        if character.isnumeric():
            first_digit = character
            break

    for character in line[::-1]:
        if character.isnumeric():
            last_digit = character
            break

    numbers.append(int(first_digit + last_digit))


result = 0
for number in numbers:
    result = result + number

print("Result for part one is: " + str(result))

# part two

numbers_re = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

numbers_two = []

for line in input:
    for n_re in numbers_re:
        line = re.sub(n_re, str(n_re) + (numbers_re[n_re]) + str(n_re), line)

    for character in line:
        if character.isnumeric():
            first_digit = character
            break

    for character in line[::-1]:
        if character.isnumeric():
            last_digit = character
            break

    numbers_two.append(int(first_digit + last_digit))


result = 0
for number in numbers_two:
    result = result + number

print("Result for part two is: " + str(result))
