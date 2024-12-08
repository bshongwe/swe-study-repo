#!/usr/bin/env python3

import os


def count_x_mas(grid):
    """
    Count occurrences of X-MAS patterns in the grid.
    
    The pattern forms an 'X' with 'MAS' on both diagonals intersecting at 'A'.
    For each 'A' in the grid, we check the two diagonal directions.
    
    :param grid: 2D list of characters representing the word search.
    :return: Total count of X-MAS patterns.
    """
    rows = len(grid)
    cols = len(grid[0])
    counter = 0

    def is_valid_x_mas(x, y):
        """
        Check if an 'X-MAS' pattern is centered at (x, y).
        """
        part1 = False
        part2 = False

        # Check bounds for diagonals
        if (x - 1 >= 0 and y - 1 >= 0 and x + 1 < rows and y + 1 < cols):
            # Top-left to bottom-right diagonal
            if (grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S") or \
               (grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M"):
                part1 = True

            # Top-right to bottom-left diagonal
            if (grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S") or \
               (grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M"):
                part2 = True

        return part1 and part2

    # Traverse grid and count occurrences
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A" and is_valid_x_mas(x, y):
                counter += 1

    return counter


def load_grid(file_path):
    """
    Load a word search grid from a file.

    :param file_path: Path to the input file containing the word search.
    :return: 2D list of characters representing the grid.
    """
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


if __name__ == "__main__":
    # Dynamically resolve file path relative to the script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "input_file.csv")

    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
    else:
        # Load grid from file
        grid = load_grid(file_path)

        # Count occurrences of 'X-MAS'
        count = count_x_mas(grid)
        print(f"Total occurrences of X-MAS patterns: {count}")
