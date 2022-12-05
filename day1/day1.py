with open("./day1/day1.txt", "r") as f:
    data = f.read().splitlines()

# part 1
elf_dict = {}
# each new line means there is a new elf

elf_count = 0
tmp_total = 0
for group in data:
    # when there is an empty line, that means it is a new group
    if group != "":
        # check if elf is in the dictionary
        if elf_count not in elf_dict:
            elf_dict[elf_count] = 0
        elf_dict[elf_count] += int(group)

    if group == "":
        elf_count += 1
    

top_elves = sorted(elf_dict.items(), key=lambda x: x[1], reverse=True)
print("Part 1: ", top_elves[0][1])
# get sum top 3
top_3 = top_elves[:3]
print("Part 2: ", sum([x[1] for x in top_3]))