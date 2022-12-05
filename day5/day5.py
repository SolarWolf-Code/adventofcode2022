with open("./day5/day5.txt", "r") as f:
    data = f.read().splitlines()

# keep only from line 11 onward

controls = data[10:]
crates = data[:11]





total_crates_stack = []
for line in crates:
    # check if the line has a number
    for i in line:
        if i.isdigit():
            # get the highest number present in line
            total_crates_stack.append(int(i))

total_crates_stack = max(total_crates_stack)

"""
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9 
"""
# all crates for stack 1 are in index 1 on their respective line
# all crates for stack 2 are in index 5 on their respective line
# they go up by 4 each time

stack_indexs = {}
last_index = 0
for i in range(1, total_crates_stack+1):
    if i == 1:
        stack_indexs[i] = 1
        last_index = 1
    else:
        last_index += 4
        stack_indexs[i] = last_index


# go through each line in crates and check if the index in stack_indexs is a letter
# if it is, add it to the stack
stacks = {}
contains_num = False
for line in crates:
    for i in line:
        if i.isdigit():
            contains_num = True
            break

    if not contains_num:
        for index in stack_indexs.values():
            if line[index].isalpha():
                # get the key that the value belongs to in stack_indexs
                key = list(stack_indexs.keys())[list(stack_indexs.values()).index(index)]
                if key not in stacks:
                    stacks[key] = [line[index]]
                else:
                    stacks[key].append(line[index])

# now use the controls to move the crates around from stack to stack
for line in controls:
    move_amt = int(line.split(" ")[1])
    orgin_stack = int(line.split(" ")[3])
    dest_stack = int(line.split(" ")[5])
    # move the crates from orgin_stack to dest_stack. use list slicing
    for i in range(move_amt):
        # pop the first item
        item = stacks[orgin_stack].pop(0)
        # add to the beginning of the dest_stack
        stacks[dest_stack].insert(0, item)
    

# order the stacks from smallest to largest key
stacks = {k: v for k, v in sorted(stacks.items(), key=lambda item: item[0])}
# print the first crate of each stack
result = ""
for stack in stacks.values():
    result += stack[0]
print(result)

# part 2


stacks = {}
contains_num = False
for line in crates:
    for i in line:
        if i.isdigit():
            contains_num = True
            break

    if not contains_num:
        for index in stack_indexs.values():
            if line[index].isalpha():
                # get the key that the value belongs to in stack_indexs
                key = list(stack_indexs.keys())[list(stack_indexs.values()).index(index)]
                if key not in stacks:
                    stacks[key] = [line[index]]
                else:
                    stacks[key].append(line[index])

# now use the controls to move the crates around from stack to stack
for line in controls:
    move_amt = int(line.split(" ")[1])
    orgin_stack = int(line.split(" ")[3])
    dest_stack = int(line.split(" ")[5])
    # move the crates from orgin_stack to dest_stack. use list slicing
    stacks[dest_stack] = stacks[orgin_stack][:move_amt] + stacks[dest_stack]
    stacks[orgin_stack] = stacks[orgin_stack][move_amt:]
    

# order the stacks from smallest to largest key
stacks = {k: v for k, v in sorted(stacks.items(), key=lambda item: item[0])}
# print the first crate of each stack
result = ""
for stack in stacks.values():
    result += stack[0]
print(result)