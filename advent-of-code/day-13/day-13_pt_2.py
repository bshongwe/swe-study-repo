#!/usr/bin/env python3

import re


def process_machine(block, part=1):
    """
    Process single claw machine's config, calculate the token cost
    if prize can be won.

    Args:
        block (str): Claw machine config block.
        part (int): Part of the challenge (1 or 2).

    Returns:
        int: Token cost to win prize for machine, or 0 if not possible.
    """
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))

    # Adjust prize coordinates for Part 2
    if part == 2:
        px += 10**13
        py += 10**13

    denominator = ax * by - ay * bx

    if denominator == 0:
        return 0

    ca = (px * by - py * bx) / denominator
    cb = (px - ax * ca) / bx

    # Conditions for valid ca and cb
    if ca % 1 == 0 and cb % 1 == 0:
        if part == 1:
            if ca <= 100 and cb <= 100:# Part 1 range check
                return int(ca * 3 + cb)
        elif part == 2:
            if ca >= 0 and cb >= 0:  # Part 2 range check
                return int(ca * 3 + cb)

    return 0


def calculate_total_tokens(input_file, part):
    """
    Calculate total tokens needed to win all possible prizes for a given part.

    Args:
        input_file (str): Path to input file.
        part (int): Part 1 or Part 2.

    Returns:
        int: Total tokens needed to win all prizes.
    """
    total_tokens = 0

    try:
        with open(input_file, "r") as file:
            data = file.read()

        for block in data.strip().split("\n\n"):
            total_tokens += process_machine(block, part)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return None

    return total_tokens


def main():
    """
    Main function to calculate and print results for both Part 1 and Part 2.
    """
    input_file = "input_file.csv"

    # Calculate and print results for Part 1
    part1_tokens = calculate_total_tokens(input_file, part=1)
    if part1_tokens is not None:
        print(f"Part 1: {part1_tokens}")

    # Calculate and print results for Part 2
    part2_tokens = calculate_total_tokens(input_file, part=2)
    if part2_tokens is not None:
        print(f"Part 2: {part2_tokens}")


if __name__ == "__main__":
    main()
