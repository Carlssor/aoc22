import collections
import os
import re


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


raw_stacks = []
stacks = collections.OrderedDict()
moves = []


for line_number, line in enumerate(read_data.splitlines()):
    if len(line) == 0:
        moves.extend(read_data.splitlines()[line_number + 1:])
        break

    raw_stacks.append(line)


for line_number, line in enumerate(raw_stacks[::-1]):
    if line_number == 0:
        for stack_number in line.split():
            stacks[int(stack_number)] = []
        continue

    for stack_number, possible_crate in enumerate(line[1::4], 1):
        if possible_crate != " ":
            stacks[stack_number].append(possible_crate)


for move in moves:
    match = re.search("move (\d+) from (\d+) to (\d+)", move).groups()
    crates_to_move, from_stack, to_stack = [int(val) for val in match]
    stacks[to_stack].extend(stacks[from_stack][-crates_to_move:])
    del stacks[from_stack][-crates_to_move:]


message = "".join(stack[-1] for stack in stacks.values())
print(message)