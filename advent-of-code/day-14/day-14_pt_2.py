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

    # Initialize counters for 4 quadrants
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    # Process each robot's data & calculate new position (at time=100)
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

    # Calculate final answer (multiply quadrant counts)
    answer = q1 * q2 * q3 * q4
    
    # Output result for the first part
    print("Answer for the first part:", answer)

    # Part 2: We want to find the smallest safety factor after a given time period
    smallest_answer = 999999999999
    found_at_second = 0

    # Loop through all possible seconds (WIDE * TALL time steps)
    for second in range(WIDE * TALL):  # pattern will repeat every WIDE * TALL times
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        final_grid = [[0] * WIDE for _ in range(TALL)]

        # Process each robot's position after `second` units of time
        for i in range(len(robots)):
            Px, Py, Vx, Vy = robots[i]
            new_Py, new_Px = (Px + Vx * second), (Py + Vy * second)
            
            # Apply modulo operation to keep new position within grid bounds (swap X and Y coordinates)
            new_Px, new_Py = new_Px % TALL, new_Py % WIDE
            
            final_grid[new_Px][new_Py] += 1

            vertical_middle = WIDE // 2
            horizontal_middle = TALL // 2

            # Determine which quadrant the robot is in
            if new_Px < vertical_middle and new_Py < horizontal_middle:
                q1 += 1
            if new_Px > vertical_middle and new_Py < horizontal_middle:
                q2 += 1
            if new_Px < vertical_middle and new_Py > horizontal_middle:
                q3 += 1
            if new_Px > vertical_middle and new_Py > horizontal_middle:
                q4 += 1

        # Calculate the safety factor (multiplication of quadrant counts)
        answer = q1 * q2 * q3 * q4
        
        # If the answer is smaller than the current smallest, update it
        if answer < smallest_answer:
            smallest_answer = answer
            found_at_second = second

    # Output result for the second part
    print("Found smallest safety factor:", smallest_answer)
    print("At second:", found_at_second)

# Call the main function
if __name__ == "__main__":
    main()
