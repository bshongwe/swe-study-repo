#!/usr/bin/env python3

import csv
import os


def read_map(file_path):
    """Reads map from a given CSV file and returns it as a grid."""
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        return [list(row[0]) for row in csv_reader]


def simulate_guard(grid):
    """Simulates guard's movement and returns number of visited positions."""
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
        row, col = guard_position
        dy, dx = directions[current_direction]
        next_position = (row + dy, col + dx)

        # Stop if guard leaves grid
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        # Check if the next position is blocked
        if grid[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4
        else:
            guard_position = next_position
            visited_positions.add(guard_position)

    return len(visited_positions), visited_positions


def find_all_loop_positions(grid, visited_positions):
    """
    Finds all positions where adding an obstruction causes
    guard to get stuck in loop.
    """
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find guard's starting position and direction
    guard_position = None
    guard_direction = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in "^>v<":
                guard_position = (y, x)
                guard_direction = "^>v<".index(cell)
                break
        if guard_position:
            break

    def causes_loop(obstruction_pos):
        """Checks if placing obstruction at position causes guard to loop."""
        direction_now = guard_direction
        guard_pos = guard_position
        visited_with_direction = set([(guard_pos, direction_now)])

        if grid[obstruction_pos[0]][obstruction_pos[1]] == "#":
            return False

        grid[obstruction_pos[0]][obstruction_pos[1]] = "#"
        rows, cols = len(grid), len(grid[0])

        while True:
            y, x = guard_pos
            dy, dx = directions[direction_now]
            next_position = (y + dy, x + dx)

            if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
                grid[obstruction_pos[0]][obstruction_pos[1]] = "."
                return False

            if grid[next_position[0]][next_position[1]] == "#":
                direction_now = (direction_now + 1) % 4
            else:
                guard_pos = next_position

            state = (guard_pos, direction_now)
            if state in visited_with_direction:
                grid[obstruction_pos[0]][obstruction_pos[1]] = "."
                return True

            visited_with_direction.add(state)

    loop_positions = []
    for pos in visited_positions:
        if pos != guard_position and causes_loop(pos):
            loop_positions.append(pos)

    return loop_positions


if __name__ == "__main__":
    # Absolute input CSV file path
    file_path = os.path.abspath("input_file.csv")

    # Read the map from the CSV file
    grid = read_map(file_path)

    # Part 1: Simulate guard's movement
    part_1_result, visited_positions = simulate_guard(grid)
    print(f"Part 1: {part_1_result}")

    # Part 2: Find positions causing loops
    loop_positions = find_all_loop_positions(grid, visited_positions)
    print(f"Part 2: {len(loop_positions)}")
