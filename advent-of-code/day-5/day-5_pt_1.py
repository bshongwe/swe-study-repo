#!/usr/bin/python3

import csv
import os


def parse(file_path):
    """
    Parse input CSV file into rules and updates.

    :param file_path: Path to input CSV file.
    :return: Tuple containing rules and updates.
    """
    rules = []
    updates = []

    try:
        with open(file_path, "r") as file:
            # Use CSV reader to handle the CSV format
            reader = csv.reader(file)
            content = list(reader)

            # Ensure that the content isn't empty
            if not content:
                raise ValueError("File content is empty.")
            
            # Split content by an empty line to separate rules and updates
            try:
                separator_index = content.index([])
                rules_part = content[:separator_index]
                updates_part = content[separator_index + 1:]
            except ValueError:
                raise ValueError("No empty line found to separate rules and updates.")

            # Parse rules into list of tuples of integers
            for line in rules_part:
                x, y = line[0].split("|")
                rules.append((int(x), int(y)))

            # Parse updates into lists of integers
            for line in updates_part:
                pages = line[0].split(",")
                updates.append([int(page) for page in pages])

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the path.")
        raise
    except ValueError as ve:
        print(f"Error in file content: {ve}")
        raise

    return rules, updates


def solve(rules, updates):
    """
    Solve problem by determining sum of middle pages for valid updates.

    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :param updates: List of updates, each being a list of page numbers.
    :return: Total sum of the middle page numbers for valid updates.
    """
    total = 0

    for update in updates:
        # Precompute indices for O(1) lookups
        page_indices = {}
        for index, page in enumerate(update):
            page_indices[page] = index

        is_valid = True

        # Check if all rules are satisfied for current update
        for x, y in rules:
            # When X & Y are in current update
            if x in page_indices and y in page_indices:
                if page_indices[x] > page_indices[y]:
                    is_valid = False
                    break

        if is_valid:
            # Find middle page in update
            middle_page = len(update) // 2
            total += update[middle_page]

    return total


if __name__ == "__main__":
    # Print current working directory for debugging
    print("Current working directory:", os.getcwd())

    # File path to CSV
    file_path = r"advent-of-code/day-5/input_file.csv"
    
    try:
        # Parse file and calculate result
        rules, updates = parse(file_path)
        result = solve(rules, updates)
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
