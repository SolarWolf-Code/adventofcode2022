with open("./day3/day3.txt", "r") as f:
    data = f.read().splitlines()

# each sack varies in size. We can use len(string)/2 then slice string

# use dict for char values
# a = 1, z = 26, A = 27, Z = 52
priority_vals = {}
for idx, val in enumerate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], start=1):
    priority_vals[val] = idx

both_rucksack = []
for line in data:
    first_half = line[:int(len(line)/2)]
    second_half = line[int(len(line)/2):]

    found_chars = []
    for char in first_half:
        if char in second_half and char not in found_chars:
            both_rucksack.append(char)
            found_chars.append(char)

total = 0
for char in both_rucksack:
    total += priority_vals[char]

# part 2 
line_count = 0
group = 0
groups_dict = {}
for  line in data:
    if group in groups_dict.keys():
        groups_dict[group].append(line)
    else:
        groups_dict[group] = [line]


    if line_count != 2:
        line_count += 1
    else:
        line_count = 0
        group += 1

# check common chars in each group
total_common_chars = []
for group in groups_dict:
    # check if there is common character in each of the 3 strings within the group

    first_string = groups_dict[group][0]
    second_string = groups_dict[group][1]
    third_string = groups_dict[group][2]

    # get common chars
    common_chars = []
    for char in first_string:
        if char in second_string and char in third_string and char not in common_chars:
            common_chars.append(char)
            total_common_chars.append(char)

total = 0
for char in total_common_chars:
    total += priority_vals[char]

print(total)