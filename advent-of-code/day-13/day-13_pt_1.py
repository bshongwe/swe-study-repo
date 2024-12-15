#!/usr/bin/env python3


import re


def process_machine(block):
    """
    Process single claw machine's config, calculate the token cost
    if prize can be won.

    Args:
        block (str): Claw machine config block.

    Returns:
        int: Token cost to win prize for machine, or 0 if not possible.
    """
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    denominator = ax * by - ay * bx

    if denominator == 0:
        return 0

    ca = (px * by - py * bx) / denominator
    cb = (px - ax * ca) / bx

    if ca % 1 == 0 and cb % 1 == 0 and ca <= 100 and cb <= 100:
        return int(ca * 3 + cb)

    return 0


def main():
    """
    Main function to calculate total tokens needed to win all possible prizes.
    """
    input_file = "input_file.csv"
    total_tokens = 0

    try:
        with open(input_file, "r") as file:
            data = file.read()

        for block in data.strip().split("\n\n"):
            total_tokens += process_machine(block)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(total_tokens)


if __name__ == "__main__":
    main()
