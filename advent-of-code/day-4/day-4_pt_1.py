#!/usr/bin/env python3

import os

def count_xmas(grid):
    """
    Count occurrences of the word 'XMAS' in all 8 possible directions within a grid.

    :param grid: 2D list of characters representing the word search.
    :return: Total count of occurrences of the word 'XMAS'.
    """
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    counter = 0

    def checker(x, y, dx, dy):
        """
        Check if the word 'XMAS' starts at (x, y) in direction (dx, dy).
        """
        for i in range(word_length):
            new_x = x + i * dx
            new_y = y + i * dy

            # Check bounds
            if not (0 <= new_x < rows and 0 <= new_y < cols):
                return False

            # Check character match
            if grid[new_x][new_y] != word[i]:
                return False

        return True

    # All 8 directions to check
    directions = [
        (0, 1),    # Right
        (1, 0),    # Down
        (1, 1),    # Diagonal down-right
        (1, -1),   # Diagonal down-left
        (0, -1),   # Left
        (-1, 0),   # Up
        (-1, -1),  # Diagonal up-left
        (-1, 1)    # Diagonal up-right
    ]

    # Traverse grid and count occurrences
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if checker(x, y, dx, dy):
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

        # Count occurrences of 'XMAS'
        count = count_xmas(grid)
        print(f"Total occurrences of 'XMAS': {count}")
