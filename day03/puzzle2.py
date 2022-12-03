import os


def get_priority(item: str) -> int:
    item_number = ord(item)
    if item_number >= ord("a"):
        priority = item_number - ord("a") + 1
    else:
        priority = item_number - ord("A") + 27
    return priority


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


groups = []
total_priority = 0


for index, rucksack in enumerate(read_data.splitlines()):
    if index % 3 == 0:
        groups.append([])
    groups[-1].append(rucksack)


for group in groups:
    common_items = set(group[0])
    for elf_items in group[1:]:
        common_items &= set(elf_items)
    for item in common_items:
        total_priority += get_priority(item)


print(total_priority)
