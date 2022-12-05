with open("./day2/day2.txt", "r") as f:
    data = f.read().splitlines()
# First column inputs
## Rock is A, Paper is B, Scissors is C

# Second column inputs
## Rock is X, Paper is Y, Scissors is Z
def part1_calc_points(col1, col2):
    subtotal_points = 0
    if col2 == "X":
        subtotal_points += 1
    elif col2 == "Y":
        subtotal_points += 2
    elif col2 == "Z":
        subtotal_points += 3

    # Draw
    if (col1 == "A" and col2 == "X") or (col1 == "B" and col2 == "Y") or (col1 == "C" and col2 == "Z"):
        subtotal_points += 3
    # Win
    elif (col1 == "A" and col2 == "Y") or (col1 == "B" and col2 == "Z") or (col1 == "C" and col2 == "X"):
        subtotal_points += 6
    # Lose
    elif (col1 == "A" and col2 == "Z") or (col1 == "B" and col2 == "X") or (col1 == "C" and col2 == "Y"):
        subtotal_points += 0
    return subtotal_points

def part2_calc_points(col1, col2):
    subtotal_points = 0

    # First column inputs
    ## Rock is A, Paper is B, Scissors is C

    if col2 == "X":
        # need to lose
        if col1 == "A":
            subtotal_points += 3
        elif col1 == "B":
            subtotal_points += 1
        elif col1 == "C":
            subtotal_points += 2

        subtotal_points += 0
    elif col2 == "Y":
        # need to draw
        if col1 == "A":
            subtotal_points += 1
        elif col1 == "B":
            subtotal_points += 2
        elif col1 == "C":
            subtotal_points += 3
        
        subtotal_points += 3
    elif col2 == "Z":
        # need to win
        if col1 == "A":
            subtotal_points += 2
        elif col1 == "B":
            subtotal_points += 3
        elif col1 == "C":
            subtotal_points += 1

        subtotal_points += 6
    return subtotal_points




total_points = 0
current_round = 0
for line in data:
    cols = line.split(" ")
    col1 = cols[0] 
    col2 = cols[1] 
    #subtotal_points = part1_calc_points(col1, col2)
    subtotal_points = part2_calc_points(col1, col2)


    total_points += subtotal_points

print("Total points:", total_points)

# part 2
# x lose, y draw, z win
