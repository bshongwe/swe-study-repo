#!/usr/bin/env python3

import sys
from collections import deque

# Directions for moving up, right, down, left
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def calculate_price(grid, use_sides=False):
    R, C = len(grid), len(grid[0])
    SEEN = set()
    total_price = 0

    # BFS to calculate area and perimeter/sides for each region
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        SEEN.add((start_r, start_c))
        area = 0
        fence = 0  # Fence can mean either perimeter or sides
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
                        fence += 1  # Different type counts towards fence
                else:
                    fence += 1  # Out of bounds counts as fence

            # For Part Two, count each adjacent region connection as a side
            if use_sides:
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    if not (0 <= rr < R and 0 <= cc < C) or grid[rr][cc] != plant_type:
                        fence += 1

        return area, fence

    # Traverse entire grid
    for r in range(R):
        for c in range(C):
            if (r, c) not in SEEN:
                area, fence = bfs(r, c)
                total_price += area * fence

    return total_price


def main():
    infile = sys.argv[1] if len(sys.argv) > 1 else "input_file.csv"
    with open(infile, "r") as f:
        grid = [line.strip() for line in f.readlines()]

    # Calculate prices for both parts
    part_one_price = calculate_price(grid, use_sides=False)  # Perimeter-based pricing
    part_two_price = calculate_price(grid, use_sides=True)   # Sides-based pricing

    print(f"Part One Total Price: {part_one_price}")
    print(f"Part Two Total Price: {part_two_price}")


if __name__ == "__main__":
    main()
