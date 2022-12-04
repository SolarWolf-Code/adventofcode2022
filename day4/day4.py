with open("/home/wolf/Desktop/adventofcode/day4.txt", "r") as f:
    data = f.read().splitlines()



total = 0
for lines in data:
    pairs = lines.split(",")
    elf1 = pairs[0]
    elf2 = pairs[1]

    elf1_sections = set()
    for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1):
        # add to the set
        elf1_sections.add(i)
    elf2_sections = set()
    for i in range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1):
        # add to the set
        elf2_sections.add(i)
    # check complete intersections. Example: {1,2,3,4,5} and {3,4,5,6,7} should return {3,4,5}
    # check if there is an intersection
    if elf1_sections.intersection(elf2_sections):
        len_intersection = len(elf1_sections.intersection(elf2_sections))
        if len_intersection == len(elf1_sections) or len_intersection == len(elf2_sections):
            total += 1


total = 0
for lines in data:
    pairs = lines.split(",")
    elf1 = pairs[0]
    elf2 = pairs[1]

    elf1_sections = set()
    for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1):
        # add to the set
        elf1_sections.add(i)
    elf2_sections = set()
    for i in range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1):
        # add to the set
        elf2_sections.add(i)
    # check complete intersections. Example: {1,2,3,4,5} and {3,4,5,6,7} should return {3,4,5}
    # check if there is an intersection
    if elf1_sections.intersection(elf2_sections):
        total += 1

print(total)