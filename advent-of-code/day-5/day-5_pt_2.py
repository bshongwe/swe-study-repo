def reorder(update, rules):
    """
    Reorder an update based on the given rules.

    :param update: A list of page numbers.
    :param rules: List of tuples (X, Y) where X must come before Y.
    :return: A reordered update list.
    """
    page_set = set(update)  # Pages in the update for quick lookup
    dependencies = {page: [] for page in update}  # Track dependencies for each page

    for x, y in rules:
        if x in page_set and y in page_set:
            dependencies[y].append(x)  # Y depends on X

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

    sorted_pages.reverse()  # Reverse to get the correct order
    return sorted_pages


def solve_part_two(rules, updates):
    """
    Solve Part Two by reordering incorrectly-ordered updates and summing middle pages.

    :param rules: List of tuples (X, Y) where X must be printed before Y.
    :param updates: List of updates, each being a list of page numbers.
    :return: Total sum of middle page numbers for reordered incorrect updates.
    """
    total = 0

    for update in updates:
        # Precompute indices for O(1) lookups
        page_indices = {page: idx for idx, page in enumerate(update)}

        is_valid = True
        for x, y in rules:
            if x in page_indices and y in page_indices:
                if page_indices[x] > page_indices[y]:
                    is_valid = False
                    break

        if not is_valid:
            # Reorder the update
            fixed_update = reorder(update, rules)
            middle_page = len(fixed_update) // 2
            total += fixed_update[middle_page]

    return total


if __name__ == "__main__":
    # Print current working directory for debugging
    print("Current working directory:", os.getcwd())

    # File path relative to current working directory
    file_path = "input_file.csv"

    try:
        # Parse file
        rules, updates = parse(file_path)

        # Solve Part Two
        result_part_two = solve_part_two(rules, updates)
        print(f"Part Two Result: {result_part_two}")
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
