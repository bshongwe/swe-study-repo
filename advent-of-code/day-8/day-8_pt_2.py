#!/usr/bin/env python3

import os
from collections import defaultdict


def read_map(file_path):
    """
    Reads the CSV map file and returns a list of lines.
    """
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


def calculate_antinodes(lines):
    """
    Calculates number of unique antinodes within grid
    based on rules of Part Two of challenge.
    """
    valid_antenna_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    antennas = []
    
    # Identify antenna positions and frequencies
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in valid_antenna_chars:
                antennas.append((x, y, char))
    
    # Group antennas by frequency
    frequency_map = defaultdict(list)
    for x, y, freq in antennas:
        frequency_map[freq].append((x, y))

    unique_antinodes = set()

    for freq, positions in frequency_map.items():
        # Include each antenna as an antinode, unless only one of its frequency
        unique_antinodes.update(positions)

        if len(positions) < 2:
            continue

        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                step_x = x2 - x1
                step_y = y2 - y1

                # Compute intermediate positions along the straight line
                k = 1
                while True:
                    antinode1 = (x1 - k * step_x, y1 - k * step_y)
                    antinode2 = (x2 + k * step_x, y2 + k * step_y)

                    valid = False
                    if 0 <= antinode1[0] < len(lines[0]) and 0 <= antinode1[1] < len(lines):
                        unique_antinodes.add(antinode1)
                        valid = True
                    if 0 <= antinode2[0] < len(lines[0]) and 0 <= antinode2[1] < len(lines):
                        unique_antinodes.add(antinode2)
                        valid = True
                    
                    if not valid:
                        break
                    k += 1

    return len(unique_antinodes)


def main():
    """
    Main function to compute the unique antinodes count.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input_file.csv")

    lines = read_map(file_path)
    antinode_count = calculate_antinodes(lines)

    print(f"Number of unique antinodes: {antinode_count}")


if __name__ == "__main__":
    main()
