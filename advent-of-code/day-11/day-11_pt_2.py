#!/usr/bin/env python3


def read_stones(file_path):
    """
    Read the list of initial stones from a file.
    Handles both space-separated and comma-separated values.
    """
    with open(file_path, "r") as file:
        content = file.read().strip()
        # Split by whitespace and convert to integers
        return [int(stone) for stone in content.split()]


def count_stones_after_blinks(stone, blinks, cache):
    """
    Efficiently count the number of stones produced by a single stone
    after a given number of blinks using memoization.
    """
    if blinks == 0:
        return 1

    if (stone, blinks) in cache:
        return cache[(stone, blinks)]

    if stone == 0:
        # Rule 1: 0 becomes 1
        result = count_stones_after_blinks(1, blinks - 1, cache)
    elif len(str(stone)) % 2 == 0:
        # Rule 2: Even digits split into two stones
        half_len = len(str(stone)) // 2
        left = int(str(stone)[:half_len])
        right = int(str(stone)[half_len:])
        result = (
            count_stones_after_blinks(left, blinks - 1, cache)
            + count_stones_after_blinks(right, blinks - 1, cache)
        )
    else:
        # Rule 3: Multiply by 2024
        result = count_stones_after_blinks(stone * 2024, blinks - 1, cache)

    cache[(stone, blinks)] = result
    return result


def total_stones(initial_stones, blinks):
    """
    Calculate the total number of stones after a given number of blinks.
    """
    cache = {}
    return sum(count_stones_after_blinks(stone, blinks, cache) for stone in initial_stones)


def main():
    """
    Main execution flow.
    """
    file_path = "input_file.csv"

    # Read initial stones from CSV
    initial_stones = read_stones(file_path)

    # Part 1: Simulate 25 blinks
    part_1_blinks = 25
    part_1_result = total_stones(initial_stones, part_1_blinks)
    print(f"Part 1: After {part_1_blinks} blinks, there are {part_1_result} stones.")

    # Part 2: Simulate 75 blinks
    part_2_blinks = 75
    part_2_result = total_stones(initial_stones, part_2_blinks)
    print(f"Part 2: After {part_2_blinks} blinks, there are {part_2_result} stones.")


if __name__ == "__main__":
    main()
