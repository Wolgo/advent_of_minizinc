from minizinc import Model, Solver, Instance
import re

# Switch between example and real instance.
file = open('example_input.txt', 'r')
# file = open('input.txt', 'r')

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

    # Addition for part b, set max_value in groups to limit search space.
    instance["max_value"] = max(groups)

    groups5 = groups.copy()
    groups5.extend(groups)
    groups5.extend(groups5)
    groups5.extend(groups)
    instance["length_groups"] = len(groups5)
    instance["groups"] = groups5
    measurements = re.findall('[.#?]', line)

    # Remap Character to Integers, so MiniZinc can handle them.
    for idx, value in enumerate(measurements):
        if value == '.':
            measurements[idx] = 1
        elif value == '#':
            measurements[idx] = 2
        elif value == '?':
            measurements[idx] = 3
    measurements5 = measurements.copy()

    for j in range(1, 5):
        measurements5.extend([3])
        measurements5.extend(measurements)

    # Part B: Remove any consecutive working machines to limit search space.
    new_measures = []
    for idx, value in enumerate(measurements5):
        if idx != len(measurements5) - 1:
            if value != 1 or measurements5[idx + 1] != 1:
                new_measures.append(value)
        else:
            new_measures.append(value)

    instance["length_measurements"] = len(new_measures)
    instance["measurements"] = list(map(int, new_measures))

    # find all Solutions instead of only 1
    result = instance.solve(all_solutions=True)
    # Keep track of the count
    count += len(result.solution)
    # Show Progress to ensure we do know when we should improve performance
    i += 1
    print("solved " + str(i) + " out of " + str(all))
    print(len(result.solution))

print(count)

