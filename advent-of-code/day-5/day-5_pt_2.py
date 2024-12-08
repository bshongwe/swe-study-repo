#!/usr/bin/python3
import os
import logging
from collections import defaultdict


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


def validate_update(update, rules):
    """
    Validate update based on given rules.

    :param update: A list of page numbers.
    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :return: Boolean indicating whether the update is valid.
    """
    page_indices = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in page_indices and y in page_indices:
            if page_indices[x] > page_indices[y]:
                return False

    return True


def reorder_update(update, rules):
    """
    Reorder update based on given rules using topological sorting.

    :param update: A list of page numbers.
    :param rules: List of tuples (X, Y) where X must come before Y.
    :return: A reordered update list.
    """
    page_set = set(update)
    dependencies = defaultdict(list)

    for x, y in rules:
        if x in page_set and y in page_set:
            dependencies[y].append(x)

    # Topological sort to reorder pages
    sorted_pages = []
    visited = set()

    def visit(page):
        if page in visited:
            return
        visited.add(page)
        for dependency in dependencies[page]:
            visit(dependency)
        sorted_pages.append(page)

    for page in update:
        visit(page)

    sorted_pages.reverse()
    return sorted_pages


def solve(rules, updates):
    """
    Solve Part One by summing middle pages of valid updates.

    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :param updates: List of updates, each being a list of page numbers.
    :return: Total sum of middle page numbers for valid updates.
    """
    total = 0
    for update in updates:
        if validate_update(update, rules):
            middle_page = len(update) // 2
            total += update[middle_page]
    return total


def solve_part_two(rules, updates):
    """
    Solve Part Two by summing middle pages of reordered invalid updates.

    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :param updates: List of updates, each being a list of page numbers.
    :return: Total sum of middle page numbers for reordered invalid updates.
    """
    total = 0
    for update in updates:
        if not validate_update(update, rules):
            reordered_update = reorder_update(update, rules)
            middle_page = len(reordered_update) // 2
            total += reordered_update[middle_page]
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
        # Parse file
        rules, updates = parse(file_path)

        # Solve Part One
        part_one_result = solve(rules, updates)
        logging.info(f"Part One Result: {part_one_result}")

        # Solve Part Two
        part_two_result = solve_part_two(rules, updates)
        logging.info(f"Part Two Result: {part_two_result}")

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}. Please check the file path.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
