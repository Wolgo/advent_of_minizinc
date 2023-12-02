import re

# Switch between example and real instance.
# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')


result = 0
for line in file.readlines():
    # Read Game ID, as the problem does not stats ids are just 1 and increasing
    game = int(re.findall('Game (\d*)', line)[0])

    # Check if the highest value of a color in each game does not exceed the max.
    if max(list(map(int, re.findall('(\d*) blue', line)))) <= 14 and max(
            list(map(int, re.findall('(\d*) red', line)))) <= 12 and max(
            list(map(int, re.findall('(\d*) green', line)))) <= 13:
        result += game

print(result)
