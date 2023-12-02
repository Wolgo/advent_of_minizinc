import re

# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')

lines = file.readlines()

result = 0
for line in lines:
    # Find the biggest numbers and multiply and add to result.
    result += max(list(map(int, re.findall('(\d*) blue', line)))) * \
              max(list(map(int, re.findall('(\d*) red', line)))) * \
              max(list(map(int, re.findall('(\d*) green', line))))

print(result)
