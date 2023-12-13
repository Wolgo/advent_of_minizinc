from minizinc import Model, Solver, Instance
import re

# Switch between example and real instance.
# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')

# Setup Minizinc
model = Model("Day12.mzn")
gecode = Solver.lookup("gecode")

lines = file.readlines()

count = 0
i = 0
all = len(lines)

for line in lines:
    # Reset the instance, as we can't put a mismatching length and array.
    instance = Instance(gecode, model)
    # Extract relevant data and put it in the model as input
    groups = list(map(int, re.findall('\d+', line)))
    instance["length_groups"] = len(groups)
    instance["groups"] = groups
    measurements = re.findall('[.#?]', line)
    instance["length_measurements"] = len(measurements)

    # Addition for part b, set max_value in groups to limit search space.
    instance["max_value"] = max(groups)

    # Remap Character to Integers, so MiniZinc can handle them.
    for idx, value in enumerate(measurements):
        if value == '.':
            measurements[idx] = 1
        elif value == '#':
            measurements[idx] = 2
        elif value == '?':
            measurements[idx] = 3
    instance["measurements"] = list(map(int, measurements))

    # find all Solutions instead of only 1
    result = instance.solve(all_solutions=True)
    # Keep track of the count
    count += len(result.solution)
    # Show Progress to ensure we do know when we should improve performance
    i += 1
    print("solved " + str(i) + " out of " + str(all))

print(count)

