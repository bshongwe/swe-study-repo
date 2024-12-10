#!/usr/bin/env python3

import argparse

def read_map(file_path):
    """
    Reads the topographic map from a file and returns it as a 2D list.

    Args:
        file_path (str): Path to the input file.

    Returns:
        list: 2D list representing the height map.
    """
    height_map = []
    with open(file_path, "r") as file:
        for line in file:
            height_map.append(list(map(int, line.strip())))
    return height_map

def find_trailheads(height_map):
    """
    Finds all positions in the height map with height 0.

    Args:
        height_map (list): 2D list representing the height map.

    Returns:
        list: List of tuples representing the coordinates of trailheads.
    """
    trailheads = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(height_map, x, y, current_height, visited):
    """
    Checks if a move to a new position is valid.

    Args:
        height_map (list): 2D list representing the height map.
        x (int): Row index of the new position.
        y (int): Column index of the new position.
        current_height (int): Current height in the path.
        visited (set): Set of visited positions.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    rows, cols = len(height_map), len(height_map[0])
    return (0 <= x < rows and 0 <= y < cols and
            (x, y) not in visited and
            height_map[x][y] == current_height + 1)

def dfs(height_map, x, y, visited):
    """
    Performs depth-first search to find all reachable height 9 positions.

    Args:
        height_map (list): 2D list representing the height map.
        x (int): Starting row index.
        y (int): Starting column index.
        visited (set): Set of visited positions.

    Returns:
        int: Number of reachable height 9 positions.
    """
    stack = [(x, y, 0)]  # (x, y, current height)
    reachable_nines = set()

    while stack:
        cx, cy, current_height = stack.pop()

        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))

        if height_map[cx][cy] == 9:
            reachable_nines.add((cx, cy))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # left, right, up, down
            new_x, new_y = cx + dx, cy + dy
            if is_valid_move(height_map, new_x, new_y, current_height, visited):
                new_height = height_map[new_x][new_y]
                stack.append((new_x, new_y, new_height))

    return len(reachable_nines)

def calculate_trailhead_scores(height_map):
    """
    Calculates the total score of all trailheads in the height map.

    Args:
        height_map (list): 2D list representing the height map.

    Returns:
        int: Total score of all trailheads.
    """
    trailheads = find_trailheads(height_map)
    total_score = 0

    for trailhead in trailheads:
        visited = set()
        total_score += dfs(height_map, trailhead[0], trailhead[1], visited)

    return total_score

def main():
    """
    Main function to handle argument parsing and execution.
    """
    parser = argparse.ArgumentParser(description="Calculate trailhead scores.")
    parser.add_argument("file_path", type=str, help="Path to the input CSV file.")
    args = parser.parse_args()

    try:
        height_map = read_map(args.file_path)
        total_score = calculate_trailhead_scores(height_map)
        print(f"Total Trailhead Score: {total_score}")
    except FileNotFoundError:
        print(f"Error: File not found: {args.file_path}")
    except ValueError:
        print("Error: Invalid file format. Ensure the file contains integers.")

if __name__ == "__main__":
    main()
