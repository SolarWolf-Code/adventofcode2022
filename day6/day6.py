with open("./day6/day6.txt", "r") as f:
    data = f.read().splitlines()

data = data[0] # first line

found_idx = 0
for idx, char in enumerate(data):
    # 4 connecting chars
    four_chars = data[idx:idx+4]
    if len(set(four_chars)) == 4:
        found_idx = idx+4
        print(found_idx)
        break

# part 2
found_idx = 0
for idx, char in enumerate(data):
    # 4 connecting chars
    four_chars = data[idx:idx+14]
    if len(set(four_chars)) == 14:
        found_idx = idx+14
        print(found_idx)
        break