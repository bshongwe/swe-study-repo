#!/usr/bin/python3

def count_word_occurrences(grid, word):
    """
    Counts all occurrences of word in grid in all 8 directions.

    :param grid: 2D list of chars representing word search.
    :param word: Word to search for.
    :return: Total count of occurrences of word.
    """
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal up-left
        (-1, 1)   # Diagonal up-right
    ]

    def is_valid(x, y):
        """Checks if coordinates are within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        """Searches for word starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count


def main():
    """Main func to run word search analysis."""
    # Example word search grid
    grid = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]

    # Converts grid to list of lists
    grid = [list(row) for row in grid]

    # Word to search for
    word = "XMAS"

    # Finds and prints total occurrences
    total_occurrences = count_word_occurrences(grid, word)
    print(f"Total occurrences of '{word}': {total_occurrences}")


if __name__ == "__main__":
    main()
