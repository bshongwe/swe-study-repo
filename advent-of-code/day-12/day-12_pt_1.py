#!/usr/bin/env python3

import sys
from collections import deque

# Directions for moving up, right, down, left
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def calculate_price(grid):
    R, C = len(grid), len(grid[0])
    SEEN = set()
    total_price = 0

    # BFS to calculate area and perimeter for each region
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        SEEN.add((start_r, start_c))
        area = 0
        perimeter = 0
        plant_type = grid[start_r][start_c]

        while queue:
            r, c = queue.popleft()
            area += 1

            # Check all 4 directions
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if grid[rr][cc] == plant_type and (rr, cc) not in SEEN:
                        SEEN.add((rr, cc))
                        queue.append((rr, cc))
                    elif grid[rr][cc] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1

        return area, perimeter

    # Traverse entire grid
    for r in range(R):
        for c in range(C):
            if (r, c) not in SEEN:
                area, perimeter = bfs(r, c)
                total_price += area * perimeter

    return total_price


def main():
    infile = sys.argv[1] if len(sys.argv) > 1 else "input_file.csv"
    with open(infile, "r") as f:
        grid = [line.strip() for line in f.readlines()]

    total_price = calculate_price(grid)
    print(total_price)


if __name__ == "__main__":
    main()
