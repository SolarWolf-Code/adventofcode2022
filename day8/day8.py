with open("./day8/day8.txt", "r") as f:
    data = f.read()

# Split the input string into individual lines
lines = data.strip().split("\n")

# Create the grid of trees
grid = []
for line in lines:
    # Split the line into individual characters and convert each character to an integer
    grid.append([int(c) for c in line])


# Function to check if a tree is visible from the left, right, top, or bottom
def is_visible(tree, row, col, grid):
    # Check if the tree is already on the edge of the grid
    if row == 0 or row == len(grid)-1 or col == 0 or col == len(grid[0])-1:
        return True

    # Check if tree is visible from the left
    for i in range(col-1, -1, -1):
        if grid[row][i] >= tree:
            break
    else:
        return True

    # Check if tree is visible from the right
    for i in range(col+1, len(grid[0])):
        if grid[row][i] >= tree:
            break
    else:
        return True

    # Check if tree is visible from the top
    for i in range(row-1, -1, -1):
        if grid[i][col] >= tree:
            break
    else:
        return True

    # Check if tree is visible from the bottom
    for i in range(row+1, len(grid)):
        if grid[i][col] >= tree:
            break
    else:
        return True

    # Tree is not visible from any direction
    return False

# Function to count the number of visible trees
def count_visible_trees(grid):
    count = 0
    # Iterate through each element in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check if the tree at this position is visible
            if is_visible(grid[row][col], row, col, grid):
                count += 1
    return count

# Count the number of visible trees
print(count_visible_trees(grid)) # Expected output: 21

# part 2

# Split the input string into individual lines
with open("./day8/day8.txt", "r") as f:
    data = f.read()
lines = data.strip().split("\n")

# Create the grid of trees
grid = []
for line in lines:
    # Split the line into individual characters and convert each character to an integer
    grid.append([int(c) for c in line])

def check_visibility(row, col, grid):
    v = grid[row][col]
    total_up = 0
    for i in range(row-1,-1, -1):
        total_up +=1
        if grid[i][col] >= v:
            break
    
    total_down = 0
    for i in range(row+1, len(grid)):
        total_down +=1
        if grid[i][col] >= v:
            break
    
    total_left = 0
    for i in range(col-1,-1, -1):
        total_left +=1
        if grid[row][i] >= v:
            break
    
    total_right = 0
    for i in range(col+1, len(grid[0])):
        total_right+=1
        if grid[row][i] >= v:
            break
    
    return total_up*total_down*total_left*total_right

max_score = 0

for row in range(len(grid)):
    for col in range(len(grid)):
        max_score = max(check_visibility(row,col,grid),max_score)
    
print(max_score)
