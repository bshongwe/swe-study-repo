#!/usr/bin/python3
import os
import logging


def parse(file_path):
    """
    Parse input CSV file into rules and updates.

    :param file_path: Path to input CSV file.
    :return: Tuple containing rules and updates.
    """
    with open(file_path, "r") as file:
        content = file.read().strip()

    rules_part, updates_part = content.split("\n\n")

    # Parse rules into a list of tuples of integers
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y)))

    # Parse updates into lists of integers
    updates = []
    update_lines = updates_part.splitlines()
    for line in update_lines:
        pages = line.split(",")
        updates.append([int(page) for page in pages])

    return rules, updates


def solve(rules, updates):
    """
    Solve problem by determining sum of middle pages for valid updates.

    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :param updates: List of updates, each being a list of page numbers.
    :return: Total sum of middle page numbers for valid updates.
    """
    total = 0

    for update in updates:
        # Precompute indices for O(1) lookups
        page_indices = {page: idx for idx, page in enumerate(update)}

        is_valid = True
        for x, y in rules:
            # Dictionary allows O(1) membership checks
            if x in page_indices and y in page_indices:
                if page_indices[x] > page_indices[y]:
                    is_valid = False
                    break

        if is_valid:
            middle_page = len(update) // 2
            total += update[middle_page]

    return total


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    # Print current working directory for debugging
    current_dir = os.getcwd()
    logging.info(f"Current working directory: {current_dir}")

    # File path relative to current working directory
    file_path = os.path.join(current_dir, "input_file.csv")

    try:
        # Parse file and calculate result
        rules, updates = parse(file_path)
        result = solve(rules, updates)
        logging.info(f"Result: {result}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}. Please check the file path.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
