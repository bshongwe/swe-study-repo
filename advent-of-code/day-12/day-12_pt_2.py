#!/usr/bin/env python3


import sys
from collections import deque


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_input(file_path):
    """
    Parse garden map from CSV file.

    Args:
        file_path (str): Input CSV file path.

    Returns:
        list[list[str]]: 2D list representing garden map.
    """
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]


def calculate_prices(grid):
    """
    Calculate prices for Part 1 & Part 2.

    Args:
        grid (list[list[str]]): 2D list representing garden map.

    Returns:
        tuple[int, int]: Total prices for Part 1 & Part 2.
    """
    R, C = len(grid), len(grid[0])
    SEEN = set()
    part_one_price = 0
    part_two_price = 0

    for r in range(R):
        for c in range(C):
            if (r, c) in SEEN:
                continue

            Q = deque([(r, c)])
            area = 0
            perimeter = 0
            PERIM = dict()

            while Q:
                r2, c2 = Q.popleft()
                if (r2, c2) in SEEN:
                    continue
                SEEN.add((r2, c2))
                area += 1
                for dr, dc in DIRS:
                    rr, cc = r2 + dr, c2 + dc
                    if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == grid[r2][c2]:
                        Q.append((rr, cc))
                    else:
                        perimeter += 1
                        if (dr, dc) not in PERIM:
                            PERIM[(dr, dc)] = set()
                        PERIM[(dr, dc)].add((r2, c2))

            sides = 0
            for k, vs in PERIM.items():
                SEEN_PERIM = set()
                for (pr, pc) in vs:
                    if (pr, pc) not in SEEN_PERIM:
                        sides += 1
                        Q = deque([(pr, pc)])
                        while Q:
                            r2, c2 = Q.popleft()
                            if (r2, c2) in SEEN_PERIM:
                                continue
                            SEEN_PERIM.add((r2, c2))
                            for dr, dc in DIRS:
                                rr, cc = r2 + dr, c2 + dc
                                if (rr, cc) in vs:
                                    Q.append((rr, cc))

            part_one_price += area * perimeter
            part_two_price += area * sides

    return part_one_price, part_two_price


def main():
    """
    Main function call.

    Reads input file, calculates total fencing cost for Part 1 & Part 2, and
    prints results.
    """
    if len(sys.argv) != 2:
        print("Usage: python day-12_pt_2.py <input_file.csv>")
        return

    file_path = sys.argv[1]
    garden_map = parse_input(file_path)
    part_one_price, part_two_price = calculate_prices(garden_map)
    print(f"Part One Total Price: {part_one_price}")
    print(f"Part Two Total Price: {part_two_price}")

if __name__ == '__main__':
    main()