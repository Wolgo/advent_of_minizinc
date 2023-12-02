from minizinc import Model, Solver, Instance
import numpy as np
import re

# Switch between example and real instance.
# file = open('example_input_b.txt', 'r')
file = open('input.txt', 'r')

# Setup Minizinc
model = Model("Day01a.mzn")
gecode = Solver.lookup("gecode")
instance = Instance(gecode, model)

lines = file.readlines()

# Set rows so that the minizinc array is large enough.
instance["rows"] = len(lines)

# Set cols so that the minizinc array is large enough.
cols = 0
for line in lines:
    cols = max(cols, len(line))
instance["cols"] = cols

# Dealing with chars or string is minizinc is difficult, so we set each character to 0
array = np.zeros((len(lines), cols), int)

i = 0
for line in lines:
    # Remove all characters as MiniZinc doesn't like it.
    line = re.sub("[a-z\n]", "", line)
    # Load all relevant numbers into the input array
    array[i, 0:len(line)] = np.array(list(line), int)
    i += 1

# Load array into MiniZinc
instance["input"] = array
# Solve
result = instance.solve()
print(result)
# Print Result from MiniZinc
print(result["result"])
