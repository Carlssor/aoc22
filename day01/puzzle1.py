import os


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


calories = [0]


for line in read_data.splitlines():
    if len(line) == 0:
        calories.append(0)
        continue
    calories[-1] += int(line)


print(max(calories))
