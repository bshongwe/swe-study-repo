#!/usr/bin/env python3

import argparse

def read_map(file_path):
    """Reads the height map from a CSV file."""
    try:
        with open(file_path, "r") as file:
            height_map = []
            for line in file:
                height_map.append(list(map(int, line.strip())))
        return height_map
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError(f"Invalid file format in: {file_path}")

def find_trailheads(height_map):
    """Finds all trailheads (positions with a value of 0) in the height map."""
    trailheads = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(height_map, x, y, current_height, visited):
    """Checks if a move is valid based on height map constraints."""
    rows, cols = len(height_map), len(height_map[0])
    return (0 <= x < rows and 0 <= y < cols and
            (x, y) not in visited and
            height_map[x][y] == current_height + 1)

def dfs_count_nines(height_map, x, y, visited):
    """Depth First Search to count reachable positions with value 9."""
    stack = [(x, y, 0)]
    reachable_nines = set()

    while stack:
        cx, cy, current_height = stack.pop()

        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))

        if height_map[cx][cy] == 9:
            reachable_nines.add((cx, cy))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = cx + dx, cy + dy
            if is_valid_move(height_map, new_x, new_y, current_height, visited):
                new_height = height_map[new_x][new_y]
                stack.append((new_x, new_y, new_height))

    return len(reachable_nines)

def calculate_trailhead_scores(height_map):
    """Calculates the total score of all trailheads based on reachable nines."""
    trailheads = find_trailheads(height_map)
    total_score = 0

    for trailhead in trailheads:
        visited = set()
        total_score += dfs_count_nines(height_map, trailhead[0], trailhead[1], visited)

    return total_score

def dfs_count_trails(height_map, x, y, visited):
    """Depth First Search to count distinct hiking trails."""
    rows, cols = len(height_map), len(height_map[0])

    if height_map[x][y] == 9:
        return 1

    visited.add((x, y))
    total_trails = 0
    current_height = height_map[x][y]

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < rows and 0 <= new_y < cols and
                (new_x, new_y) not in visited and
                height_map[new_x][new_y] == current_height + 1):
            total_trails += dfs_count_trails(height_map, new_x, new_y, visited.copy())

    return total_trails

def calculate_trailhead_ratings(height_map):
    """Calculates the total rating of all trailheads based on distinct trails."""
    trailheads = find_trailheads(height_map)
    total_rating = 0

    for trailhead in trailheads:
        visited = set()
        total_rating += dfs_count_trails(height_map, trailhead[0], trailhead[1], visited)

    return total_rating

def main():
    parser = argparse.ArgumentParser(description="Hiking trail map analysis.")
    parser.add_argument("file_path", help="Path to the height map CSV file.")
    args = parser.parse_args()

    try:
        height_map = read_map(args.file_path)

        # Part 1: Calculate total score based on reachable nines
        part1_score = calculate_trailhead_scores(height_map)
        print(f"Part 1 - Total Score: {part1_score}")

        # Part 2: Calculate total rating based on distinct trails
        part2_rating = calculate_trailhead_ratings(height_map)
        print(f"Part 2 - Total Rating: {part2_rating}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
