#!/usr/bin/python3
import os


def parse(file_path):
    """
    Parse input CSV file into rules and updates.

    :param file_path: Path to the input CSV file.
    :return: Tuple containing rules and updates.
    """
    with open(file_path, "r") as file:
        content = file.read().strip()

    rules_part, updates_part = content.split("\n\n")

    # Parse rules into a list of tuples of integers
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y)))  # Tuple (X, Y) appended to the list

    # Parse updates into lists of integers
    updates = []
    update_lines = updates_part.splitlines()
    for line in update_lines:
        pages = line.split(",")
        updates.append([int(page) for page in pages])

    return rules, updates


def solve(rules, updates):
    """
    Solve the problem by determining the sum of middle pages for valid updates.

    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :param updates: List of updates, each being a list of page numbers.
    :return: Total sum of middle page numbers for valid updates.
    """
    total = 0

    for update in updates:
        # Precompute indices for O(1) lookups
        page_indices = {}
        index = 0
        for page in update:
            page_indices[page] = index
            index += 1

        is_valid = True

        for x, y in rules:
            # Instead of checking membership in a list (O(P)),
            # dictionary allows O(1) membership checks.
            if x in page_indices and y in page_indices:  # If both exist in update
                if page_indices[x] > page_indices[y]:  # Rule violated
                    is_valid = False
                    break

        if is_valid:
            middle_page = len(update) // 2  # If even, take from right.
            total += update[middle_page]

    return total


if __name__ == "__main__":
    # Print current working directory for debugging
    print("Current working directory:", os.getcwd())

    # File path relative to the current working directory
    file_path = "input_file.csv"
    
    try:
        # Parse file and calculate result
        rules, updates = parse(file_path)
        result = solve(rules, updates)
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")