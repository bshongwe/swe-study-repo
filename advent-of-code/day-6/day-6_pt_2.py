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
    try:
        with open(file_path, mode="r", newline="") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                map_grid.append(list("".join(row)))
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}. Please check the file path.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}")
        raise
    return map_grid


def simulate_guard(grid, guard_position, guard_direction):
    """
    Simulates guard's patrol and calculates distinct positions visited.

    :param grid: List of lists representing map grid.
    :param guard_position: Starting position of guard.
    :param guard_direction: Initial direction guard is facing.
    :return: Set of distinct positions visited by guard.
    """
    # Direction deltas: down, right, up, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited_positions = set([guard_position])
    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate next position
        row, col = guard_position
        dy, dx = directions[guard_direction]
        next_position = (row + dy, col + dx)

        # Stop if guard leaves grid
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        # Check if next position is blocked
        if grid[next_position[0]][next_position[1]] == "#":
            guard_direction = (guard_direction + 1) % 4
        else:
            guard_position = next_position
            if guard_position in visited_positions:
                # If guard revisits a position, it is stuck in a loop
                return visited_positions
            visited_positions.add(guard_position)

    return visited_positions


def find_possible_obstruction_positions(grid, guard_position, guard_direction):
    """
    Finds all possible positions where a new obstruction can be placed to trap guard in a loop.

    :param grid: List of lists representing map grid.
    :param guard_position: Current position of guard.
    :param guard_direction: Current direction guard is facing.
    :return: A list of possible positions to place obstruction.
    """
    possible_positions = []

    # Iterate over all positions in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Skip guard's starting position
            if (row, col) == guard_position:
                continue

            # Only consider empty spaces where a new obstruction can be placed
            if grid[row][col] == ".":
                # Temporarily place the obstruction
                grid[row][col] = "O"

                # Simulate the guard's movement with the new obstruction
                visited_positions = simulate_guard(grid, guard_position, guard_direction)

                # If guard gets stuck in a loop, it is a valid obstruction position
                if len(visited_positions) < len(set([guard_position])):
                    possible_positions.append((row, col))

                # Remove obstruction after testing this position
                grid[row][col] = "."

    return possible_positions


def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Print current working directory for debugging
    current_dir = os.getcwd()
    logging.info(f"Current working directory: {current_dir}")

    # File path relative to current working directory
    file_path = os.path.join(current_dir, "input_file.csv")

    try:
        # Read map and find guard's position and direction
        grid = read_map(file_path)
        guard_position = None
        guard_direction = None

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] in "^>v<":
                    guard_position = (row, col)
                    guard_direction = "^>v<".index(grid[row][col])
                    break
            if guard_position:
                break

        # Find possible obstruction positions
        obstruction_positions = find_possible_obstruction_positions(grid, guard_position, guard_direction)

        # Log result
        logging.info(f"Number of valid obstruction positions: {len(obstruction_positions)}")

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}. Please check the file path.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
