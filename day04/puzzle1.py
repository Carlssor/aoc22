import os


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


totally_contained_sections = 0


for pair in read_data.splitlines():
    sections = []
    for section_range in pair.split(","):
        section_start, section_end = [int(val) for val in section_range.split("-")]
        sections.append((section_start, section_end))
    sections.sort(key=lambda section_range: section_range[1] - section_range[0], reverse=True)

    start_longest, end_longest = sections[0]
    for section_start, section_end in sections:
        if section_start < start_longest or section_end > end_longest:
            break
    else:
        totally_contained_sections += 1


print(totally_contained_sections)
