from minizinc import Model, Solver, Instance
import numpy as np
import re

# Switch between example and real instance.
# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')

# Setup Minizinc
model = Model("Day04b.mzn")
# Solver with bigger max int
gecode = Solver.lookup("gecode")
instance = Instance(gecode, model)

lines = file.readlines()

# Set rows so that the minizinc array is large enough.
instance["rows"] = len(lines)

numbers = list(re.findall('\d+|\|', lines[0]))

StillBefore = True
before = -1
after = 0

for number in numbers:
    if number == "|":
        StillBefore = False
    else:
        if StillBefore:
            before += 1
        else:
            after += 1

instance["before"] = before
instance["after"] = after

# Set cols so that the minizinc array is large enough.
array_winning = np.zeros((len(lines), before), int)
array_numbers = np.zeros((len(lines), after), int)

i = 0
for line in lines:
    numbers = list(re.findall('\d+', line))
    array_winning[i, 0:before] = numbers[1:before+1]
    array_numbers[i, 0:after] = numbers[before+1:before+after+1]
    i += 1

# Load array into MiniZinc
instance["winning"] = array_winning
instance["numbers"] = array_numbers
# Solve
result = instance.solve()
print(result)
# Using score to calculate more :).
score = result["score"]
array_count = np.ones(len(lines), int)
print(score)
i = 0
for x in array_count:
    print(array_count)
    print(score[i])
    j = i+1
    while j <= i+score[i]:
        array_count[j] += array_count[i]
        j += 1
    i += 1

print(sum(array_count))
