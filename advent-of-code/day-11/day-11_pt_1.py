#!/usr/bin/env python3


import csv


import csv


def read_stones(file_path):
    """
    Read the list of initial stones from a file.
    Handles both space-separated and comma-separated values.
    """
    with open(file_path, "r") as file:
        content = file.read().strip()
        # Split by whitespace and convert to integers
        return [int(stone) for stone in content.split()]


def transform_stones(stones):
    """
    Transform the list of stones according to the rules.
    """
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:  # Even number of digits
            half_len = len(str(stone)) // 2
            left = int(str(stone)[:half_len])
            right = int(str(stone)[half_len:])
            new_stones.extend([left, right])
        else:  # Multiply by 2024
            new_stones.append(stone * 2024)
    return new_stones


def simulate_blinks(initial_stones, blinks):
    """
    Simulate the blinking process for a given number of blinks.
    """
    current_stones = initial_stones
    for _ in range(blinks):
        current_stones = transform_stones(current_stones)
    return current_stones


def main():
    """
    Main execution flow.
    """
    file_path = "input_file.csv"  # Input file path
    blinks = 25  # Number of blinks to simulate

    # Read initial stones from CSV
    initial_stones = read_stones(file_path)

    # Simulate the blinking process
    final_stones = simulate_blinks(initial_stones, blinks)

    # Output the number of stones after the blinks
    print(f"After {blinks} blinks, there are {len(final_stones)} stones.")


if __name__ == "__main__":
    main()
