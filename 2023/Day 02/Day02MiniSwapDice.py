from minizinc import Model, Solver, Instance
import numpy as np
import re

# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')

# Setup Minizinc
model = Model("Day02MiniSwapDice.mzn")
gecode = Solver.lookup("gecode")
instance = Instance(gecode, model)

# Read lines
lines = file.readlines()

# Prepare an input array for MiniZinc
array = np.zeros((len(lines), 3), int)
# Set rows so that the minizinc array is large enough.
instance["rows"] = len(lines)

i = 0
for line in lines:
    # Find the biggest numbers and multiply and add to result.
    array[i, 0] = max(list(map(int, re.findall('(\d*) blue', line))))
    array[i, 1] = max(list(map(int, re.findall('(\d*) red', line))))
    array[i, 2] = max(list(map(int, re.findall('(\d*) green', line))))
    i += 1

# Load array into MiniZinc
instance["input"] = array

# Solve
result = instance.solve()
print(result)
print("Dice Used: " + str(result["result"]))
