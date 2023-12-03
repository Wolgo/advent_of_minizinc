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
char_array = np.empty((len(lines), cols), dtype=str)
number_array = np.empty((len(lines), cols), dtype=str)
number_array_2 = np.empty((len(lines), cols), dtype=str)

result = 0
i = 0

for line in lines:

    j = 0
    for char in line:
        if char not in ".\n":
            char_array[i, j] = char
        else:
            char_array[i, j] = " "

        j += 1
    i += 1

i = 0
for line in lines:
    j = 0
    for char in line:
        if char not in "1234567890. \n":
            if i > 0:
                number_array[i - 1, j] = char_array[i - 1, j]
                if j > 0:
                    number_array[i - 1, j - 1] = char_array[i - 1, j - 1]
                if j < cols - 1:
                    number_array[i - 1, j + 1] = char_array[i - 1, j + 1]
            if i < len(lines):
                number_array[i + 1, j] = char_array[i + 1, j]
                if j > 0:
                    number_array[i + 1, j - 1] = char_array[i + 1, j - 1]
                if j < cols - 1:
                    number_array[i + 1, j + 1] = char_array[i + 1, j + 1]
            if j > 0:
                number_array[i, j - 1] = char_array[i, j - 1]
            if j < cols - 1:
                number_array[i, j + 1] = char_array[i, j + 1]

        j += 1
    i += 1


first = True
while (number_array != number_array_2).any():
    if first:
        number_array_2 = number_array.copy()
        first = False
    else:
        number_array = number_array_2.copy()

    print(number_array)
    i = 0
    while i < len(lines):
        j = 0
        while j < cols:
            if number_array[i, j] in "0123456789" and number_array[i, j] != "":
                if j > 0:
                    number_array_2[i, j - 1] = char_array[i, j - 1]
                if j < cols - 1:
                    number_array_2[i, j + 1] = char_array[i, j + 1]
            j += 1
        i += 1


number_array = list(number_array)
result = ""
for i in number_array:
    for j in i:
        result += j
print(result)
print(re.findall('\\d+', result))
print(sum(map(int, re.findall('\\d+', result))))
