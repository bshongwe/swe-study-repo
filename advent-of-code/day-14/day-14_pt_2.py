#!/usr/bin/env python3

def main():
    # Constants for grid dimensions
    WIDE = 101
    TALL = 103

    # List to store robot data (position and velocity)
    robots = []

    # Open & read CSV file line by line
    with open("input_file.csv", "r") as file:
        for robot in file:
            # Split line into left and right side data
            sides = robot.split(" ")
            left_side = sides[0]
            right_side = sides[1]
            
            # Parse position (Px, Py) from left side
            left_sides = left_side.split(",")
            Px = left_sides[0].split("=")[-1]
            Py = left_sides[1]
            
            # Parse velocity (Vx, Vy) from right side
            right_sides = right_side.split(",")
            Vx = right_sides[0].split("=")[-1]
            Vy = right_sides[1].strip()
            
            # Convert position & velocity values to integers
            Px = int(Px)
            Py = int(Py)
            Vx = int(Vx)
            Vy = int(Vy)
            
            # Append parsed robot data (position and velocity) to robots list
            robots.append([Px, Py, Vx, Vy])

    # --- Part 1 ---
    # Initialize counters for 4 quadrants
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    # Process each robot's data & calculate new position
    for i in range(len(robots)):
        Px, Py, Vx, Vy = robots[i]
        
        # Calculate new position: velocity & time (100 units of time)
        new_Px = Px + Vx * 100
        new_Py = Py + Vy * 100
        
        # Apply modulo operation to keep new position within grid bounds
        new_Px, new_Py = new_Px % WIDE, new_Py % TALL
        
        # Find middle of grid (vertical and horizontal)
        vertical_middle = WIDE // 2
        horizontal_middle = TALL // 2
        
        # Determine quadrant: robot's new position
        if new_Px < vertical_middle and new_Py < horizontal_middle:
            q1 += 1
        elif new_Px > vertical_middle and new_Py < horizontal_middle:
            q2 += 1
        elif new_Px < vertical_middle and new_Py > horizontal_middle:
            q3 += 1
        elif new_Px > vertical_middle and new_Py > horizontal_middle:
            q4 += 1

    # Calculate final answer for Part 1: multiplying quadrant counts
    part1_answer = q1 * q2 * q3 * q4
    
    # Output Part 1 result
    print(f"Part 1 Answer: {part1_answer}")

    # --- Part 2 ---
    # Define the Christmas tree shape (this is an assumption; adjust based on actual challenge description)
    christmas_tree_shape = set([
        (50, 0), (51, 1), (49, 1), (52, 2), (48, 2), (53, 3), (47, 3), (54, 4), (46, 4),
        (45, 5), (55, 5), (44, 6), (56, 6), (43, 7), (57, 7), (42, 8), (58, 8), (41, 9)
    ])

    # Run simulation for up to 1000 seconds or until robots form the tree
    max_seconds = 1000
    for t in range(max_seconds):
        # Update robot positions based on their velocities
        new_positions = set()
        for Px, Py, Vx, Vy in robots:
            new_Px = Px + Vx * t
            new_Py = Py + Vy * t
            
            # Apply modulo operation to keep new position within grid bounds
            new_Px, new_Py = new_Px % WIDE, new_Py % TALL
            
            # Add the new position to the set of positions
            new_positions.add((new_Px, new_Py))
        
        # Check if the current positions match the Christmas tree shape
        if new_positions == christmas_tree_shape:
            print(f"Part 2 Answer: The robots form a Christmas tree at second {t}.")
            break
    else:
        # If no solution found within the max seconds
        print("Part 2 Answer: The robots did not form a Christmas tree within the time limit.")

# Call the main function
if __name__ == "__main__":
    main()
