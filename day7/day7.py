with open("./day7/day7.txt", "r") as f:
    data = f.read().splitlines()


file_path = []
dir_sizes = {}

for line in data:
    parts = line.strip().split()

    if parts[1] == 'cd':
        if parts[2] == '..':
            file_path.pop()
        else:
            file_path.append(parts[2])
    elif parts[1] != 'ls' and parts[0] != "dir":
        file_size = int(parts[0])
        for i in range(1, len(file_path)+1):
            dir = '/'.join(file_path[:i])
            if dir not in dir_sizes:
                dir_sizes[dir] = 0
            dir_sizes[dir] += file_size

total = 0

for i, j in dir_sizes.items():
    if j <= 100000:
        total += j

print(total)


needed_size = dir_sizes['/'] - (70000000 - 30000000)
closest_size = None

for i, j in dir_sizes.items():
    if j >= needed_size:
        if closest_size is None or j < closest_size:
            closest_size = j

print(closest_size)