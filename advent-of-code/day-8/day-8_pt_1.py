#!/usr/bin/env python3

import os
from collections import defaultdict

# Dynamically locate the input CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input_file.csv")

# Read the file and store lines
with open(file_path, "r") as file:
    lines = [line.strip() for line in file]

# Define valid antenna characters
valid_antenna_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Collect antenna positions and frequencies
antennas = [
    (x, y, char)
    for y, line in enumerate(lines)
    for x, char in enumerate(line)
    if char in valid_antenna_chars
]

# Group antennas by frequency
frequency_map = defaultdict(list)
for x, y, freq in antennas:
    frequency_map[freq].append((x, y))

# Find unique antinode locations
unique_antinodes = set()
for freq, positions in frequency_map.items():
    if len(positions) < 2:
        continue

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            step_x = x2 - x1
            step_y = y2 - y1

            antinode1 = (x1 - step_x, y1 - step_y)
            antinode2 = (x2 + step_x, y2 + step_y)

            if 0 <= antinode1[0] < len(lines[0]) and 0 <= antinode1[1] < len(lines):
                unique_antinodes.add(antinode1)
            if 0 <= antinode2[0] < len(lines[0]) and 0 <= antinode2[1] < len(lines):
                unique_antinodes.add(antinode2)

# Output the number of unique antinode locations
print(len(unique_antinodes))
