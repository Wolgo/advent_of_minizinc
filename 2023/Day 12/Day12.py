from minizinc import Model, Solver, Instance
import numpy as np
import re

# Switch between example and real instance.
# file = open('example_input.txt', 'r')
file = open('input.txt', 'r')

# Setup Minizinc
model = Model("Day12a.mzn")
# Solver with bigger max int
gecode = Solver.lookup("float")
instance = Instance(gecode, model)

lines = file.readlines()
stage = 0

array = np.empty((0, 3), int)
print(array)
for line in lines:
    if stage == 0:
        seeds = list(map(int, re.findall('\d+', line)))
        print(seeds)
        instance["seed_length"] = len(seeds)
        instance["seeds"] = seeds
        stage = 1
    elif 1 <= stage < 3:
        stage += 1
    elif 3 <= stage < 4:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["seed_to_soil_length"] = len(array)
            instance["seed_to_soil"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])
    elif 4 <= stage < 6:
        array = np.empty((0, 3), int)
        stage += 1
    elif 6 <= stage < 7:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["soil_to_fertilizer_length"] = len(array)
            instance["soil_to_fertilizer"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])
    elif 7 <= stage < 9:
        array = np.empty((0, 3), int)
        stage += 1
    elif 9 <= stage < 10:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["fertilizer_to_water_length"] = len(array)
            instance["fertilizer_to_water"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])
    elif 10 <= stage < 12:
        array = np.empty((0, 3), int)
        stage += 1
    elif 12 <= stage < 13:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["water_to_light_length"] = len(array)
            instance["water_to_light"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])
    elif 13 <= stage < 15:
        array = np.empty((0, 3), int)
        stage += 1
    elif 15 <= stage < 16:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["light_to_temperature_length"] = len(array)
            instance["light_to_temperature"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])
    elif 16 <= stage < 18:
        array = np.empty((0, 3), int)
        stage += 1
    elif 18 <= stage < 19:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["temperature_to_humidity_length"] = len(array)
            instance["temperature_to_humidity"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])
    elif 19 <= stage < 21:
        array = np.empty((0, 3), int)
        stage += 1
    elif 21 <= stage < 22:
        numbers = list(map(int, re.findall('\d+', line)))
        if len(numbers) == 0:
            instance["humidity_to_location_length"] = len(array)
            instance["humidity_to_location"] = array
            print(array)
            stage += 1
        else:
            array = np.vstack([array, numbers])

# Solve
result = instance.solve()
print(result)
# Print Result from MiniZinc
print(result["location"])
