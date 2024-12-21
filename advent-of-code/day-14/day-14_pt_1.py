#!/usr/bin/env python3

"""
Restroom Redoubt Challenge Solution.
This script simulates robot movements to calculate the safety factor.
"""
import csv
import os
import sys

def parse_input(file_path):
    """Parse the input CSV file into a list of robots with positions and velocities."""
    robots = []
    malformed_rows = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                print(f"Parsing row: {row}")  # Debug print statement
                # Adjust the parsing logic to correctly extract position and velocity
                p_part, v_part = row[0].split(" v=")
                px, py = map(int, p_part[2:].split(","))
                vx, vy = map(int, v_part.split(","))
                robots.append({"position": [px, py], "velocity": [vx, vy]})
            except (ValueError, IndexError) as e:
                print(f"Skipping malformed row: {row} (Error: {e})")
                malformed_rows.append(row)
    
    if not robots:
        raise ValueError("No valid robot data found in the input file.")

    if malformed_rows:
        print(f"Total malformed rows skipped: {len(malformed_rows)}")

    return robots

def simulate(robots, width, height, time):
    """Simulate the movement of robots for the given time."""
    for t in range(time):
        for robot in robots:
            robot["position"][0] = (robot["position"][0] + robot["velocity"][0]) % width
            robot["position"][1] = (robot["position"][1] + robot["velocity"][1]) % height
    print(f"Final positions after {time} steps: {[(robot['position'], robot['velocity']) for robot in robots]}")  # Debug print statement

def count_quadrants(robots, width, height):
    """Count the number of robots in each quadrant."""
    mid_x, mid_y = width // 2, height // 2
    quadrants = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

    for robot in robots:
        x, y = robot["position"]
        if x == mid_x or y == mid_y:
            continue  # Ignore robots exactly on the midlines
        if x > mid_x and y < mid_y:
            quadrants["Q1"] += 1
        elif x < mid_x and y < mid_y:
            quadrants["Q2"] += 1
        elif x < mid_x and y > mid_y:
            quadrants["Q3"] += 1
        elif x > mid_x and y > mid_y:
            quadrants["Q4"] += 1

    print(f"Quadrant counts: {quadrants}")  # Debug print statement
    return quadrants

def calculate_safety_factor(quadrants):
    """Calculate the safety factor from quadrant counts."""
    return quadrants["Q1"] * quadrants["Q2"] * quadrants["Q3"] * quadrants["Q4"]

def main():
    """Main function to execute the program."""
    # Check for command-line arguments
    if len(sys.argv) != 2:
        print("Usage: ./day-14_pt_1.py <input_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Grid dimensions
    width = 101
    height = 103

    # Time to simulate
    time = 100

    try:
        # Parse input
        robots = parse_input(input_file)
        print(f"Parsed {len(robots)} robots from the input file.")

        # Simulate movement
        simulate(robots, width, height, time)
        print("Simulation complete.")

        # Count quadrants
        quadrants = count_quadrants(robots, width, height)
        print("Quadrant counts:", quadrants)

        # Calculate safety factor
        safety_factor = calculate_safety_factor(quadrants)
        print("Safety Factor:", safety_factor)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
