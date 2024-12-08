#!/usr/bin/env python3
import os
import logging
import csv


def read_map(file_path):
    """
    Reads map grid from a CSV file.

    :param file_path: Path to CSV file.
    :return: List of lists representing map grid.
    """
    map_grid = []
    with open(file_path, mode="r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            map_grid.append(list("".join(row)))
    return map_grid


def simulate_guard(grid):
    """
    Simulates guard's patrol and calculates distinct positions visited.

    :param grid: List of lists representing the map grid.
    :return: Integer count of distinct positions visited by guard.
    """
    # Direction deltas: down, right, up, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find guard's starting position and direction
    guard_position = None
    current_direction = None

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in "^>v<":
                guard_position = (row, col)
                current_direction = "^>v<".index(grid[row][col])
                break
        if guard_position:
            break

    visited_positions = set([guard_position])
    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate next position
        row, col = guard_position
        dy, dx = directions[current_direction]
        next_position = (row + dy, col + dx)

        # Stop if guard leaves the grid
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        # Check if next position is blocked
        if grid[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4  # Turn right
        else:
            guard_position = next_position  # Move forward
            visited_positions.add(guard_position)

    return len(visited_positions)


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # File path relative to current working directory
    file_path = os.path.join(os.getcwd(), "input_file.csv")

    try:
        # Read the map and simulate guard's movement
        grid = read_map(file_path)
        result = simulate_guard(grid)

        # Log result
        logging.info(f"Distinct positions visited: {result}")

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}. Please check the file path.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
