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


total_priority = 0


for rucksack in read_data.splitlines():
    first_compartment = set(rucksack[:len(rucksack)//2])
    second_compartment = set(rucksack[len(rucksack)//2:])
    appears_in_both = first_compartment & second_compartment
    for item in appears_in_both:
        total_priority += get_priority(item)


print(total_priority)
