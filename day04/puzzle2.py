import os


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


overlappings = 0


for pair in read_data.splitlines():
    sections = []
    for section_range in pair.split(","):
        section_start, section_end = [int(val) for val in section_range.split("-")]
        sections.append((section_start, section_end))
    sections.sort(key=lambda section_range: section_range[0])

    for index, section in enumerate(sections[:-1]):
        current_end_section = section[1]
        next_start_section = sections[index + 1][0]
        if current_end_section < next_start_section:
            break
    else:
        overlappings += 1


print(overlappings)
