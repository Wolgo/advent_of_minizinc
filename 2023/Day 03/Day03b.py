import re
import numpy as np

# Switch between example and real instance.
# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')

lines = file.readlines()
# Set cols so that the minizinc array is large enough.
cols = 0
for line in lines:
    cols = max(cols, len(line))

# Dealing with chars or string is minizinc is difficult, so we set each character to 0
char_array = np.zeros((len(lines), cols), dtype=int)

result = 0
i = 0

for line in lines:
    list_of_numbers = re.findall("\d+", line)
    print(list_of_numbers)
    number_count = 0
    digit_count = 0
    j = 0
    for char in line:
        if char in "0123456789":
            char_array[i, j] = list_of_numbers[number_count]
            digit_count += 1
        if char in "*":
            char_array[i, j] = -1
        if number_count != len(list_of_numbers) and digit_count == len(list_of_numbers[number_count]):
            print(len(list_of_numbers[number_count]))
            print(list_of_numbers[number_count])
            number_count += 1
            digit_count = 0
        j += 1
    i += 1

i = 0
result = 0
while i < len(lines):
    j = 0
    while j < cols:
        if char_array[i, j] == -1:
            numbers = []
            if i > 0:
                numbers.append(char_array[i - 1, j])
                if j > 0 and char_array[i - 1, j] != char_array[i - 1, j - 1]:
                    numbers.append(char_array[i - 1, j - 1])
                if j < cols - 1 and char_array[i - 1, j] != char_array[i - 1, j + 1]:
                    numbers.append(char_array[i - 1, j + 1])
            if i < len(lines):
                numbers.append(char_array[i + 1, j])
                if j > 0 and char_array[i + 1, j] != char_array[i + 1, j - 1]:
                    numbers.append(char_array[i + 1, j - 1])
                if j < cols - 1 and char_array[i + 1, j] != char_array[i + 1, j + 1]:
                    numbers.append(char_array[i + 1, j + 1])
            if j > 0:
                numbers.append(char_array[i, j - 1])
            if j < cols - 1:
                numbers.append(char_array[i, j + 1])
            while 0 in numbers:
                numbers.remove(0)
            # print(numbers)
            if len(numbers) == 2:
                print(numbers)
                result += numbers[0] * numbers[1]
                print(result)
        j += 1
    i += 1
print(result)
