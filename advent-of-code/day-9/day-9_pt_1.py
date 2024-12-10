#!/usr/bin/env python3


import os

def read_disk_map(file_path):
    """Read the disk map from a CSV file."""
    with open(file_path, "r") as file:
        return file.read().strip()

def parse_disk_map(disk_map):
    """Parse the disk map into file and free space segments."""
    disk_segments = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append(("file", file_length))
        if free_length > 0:
            disk_segments.append(("free", free_length))
    return disk_segments

def build_disk_representation(disk_segments):
    """Build the initial disk representation."""
    blocks = []
    file_id = 0
    for segment, length in disk_segments:
        if segment == "file":
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(["."] * length)
    return blocks

def compact_disk(blocks):
    """Compact the disk by moving files to the left."""
    left_walker, right_walker = 0, len(blocks) - 1
    while left_walker < right_walker:
        while left_walker < len(blocks) and blocks[left_walker] != ".":
            left_walker += 1
        while right_walker >= 0 and blocks[right_walker] == ".":
            right_walker -= 1
        if left_walker < right_walker:
            blocks[left_walker], blocks[right_walker] = (
                blocks[right_walker], blocks[left_walker]
            )
    return blocks

def calculate_checksum(blocks):
    """Calculate the filesystem checksum."""
    checksum = 0
    for i, block in enumerate(blocks):
        if block != ".":
            checksum += i * block
    return checksum

def main():
    """Main function to execute the disk compaction and checksum calculation."""
    file_name = "input_file.csv"
    file_path = os.path.join(os.getcwd(), file_name)

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found in the current directory.")
        return

    disk_map = read_disk_map(file_path)
    disk_segments = parse_disk_map(disk_map)
    blocks = build_disk_representation(disk_segments)
    compacted_blocks = compact_disk(blocks)
    checksum = calculate_checksum(compacted_blocks)

    print(f"Filesystem checksum: {checksum}")

if __name__ == "__main__":
    main()
