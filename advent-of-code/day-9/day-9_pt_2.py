#!/usr/bin/env python3


import os

def read_disk_map(file_name):
    """Read and parse disk map from CSV."""
    file_path = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r") as file:
        disk_map = file.read().strip()

    return disk_map

def parse_disk_segments(disk_map):
    """Parse disk map into segments."""
    disk_segments = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append(("file", file_length))
        if free_length > 0:
            disk_segments.append(("free", free_length))
    return disk_segments

def build_disk_representation(disk_segments):
    """Build initial disk representation."""
    blocks = []
    file_positions = []
    file_id = 0
    pos = 0

    for segment, length in disk_segments:
        if segment == "file":
            blocks.extend([file_id] * length)
            file_positions.append((pos, length, file_id))
            pos += length
            file_id += 1
        else:
            blocks.extend([None] * length)
            pos += length

    return blocks, file_positions

def compact_disk_part1(blocks):
    """Compact disk for Part 1 by moving blocks individually."""
    left_walker, right_walker = 0, len(blocks) - 1

    while left_walker < right_walker:
        while left_walker < len(blocks) and blocks[left_walker] is not None:
            left_walker += 1
        while right_walker >= 0 and blocks[right_walker] is None:
            right_walker -= 1
        if left_walker < right_walker:
            blocks[left_walker], blocks[right_walker] = blocks[right_walker], None

    return calculate_checksum(blocks)

def compact_disk_part2(blocks, file_positions):
    """Compact disk for Part 2 by moving whole files."""
    # Aggregate free spaces into a list of tuples
    free_spaces = []
    current_pos = 0

    while current_pos < len(blocks):
        if blocks[current_pos] is None:
            start = current_pos
            while current_pos < len(blocks) and blocks[current_pos] is None:
                current_pos += 1
            free_spaces.append((start, current_pos - start))
        current_pos += 1

    # Move files to the leftmost valid space
    file_count = len(file_positions)
    space_count = len(free_spaces)

    for file_index in range(file_count - 1, -1, -1):
        start_pos, file_size, file_id = file_positions[file_index]
        for space_index in range(space_count):
            space_pos, space_size = free_spaces[space_index]
            if space_pos < start_pos and file_size <= space_size:
                for j in range(file_size):
                    blocks[start_pos + j] = None
                    blocks[space_pos + j] = file_id
                free_spaces[space_index] = (space_pos + file_size, space_size - file_size)
                break

    return calculate_checksum(blocks)

def calculate_checksum(blocks):
    """Calculate checksum of disk blocks."""
    checksum = 0
    for i, block in enumerate(blocks):
        if block is not None:
            checksum += i * block
    return checksum

def main():
    """Main function to execute both parts of challenge."""
    file_name = "input_file.csv"
    disk_map = read_disk_map(file_name)
    disk_segments = parse_disk_segments(disk_map)
    blocks, file_positions = build_disk_representation(disk_segments)

    # Part 1
    part1_blocks = blocks.copy()
    part1_checksum = compact_disk_part1(part1_blocks)
    print(f"Part 1 Checksum: {part1_checksum}")

    # Part 2
    part2_blocks = blocks.copy()
    part2_checksum = compact_disk_part2(part2_blocks, file_positions)
    print(f"Part 2 Checksum: {part2_checksum}")

if __name__ == "__main__":
    main()
