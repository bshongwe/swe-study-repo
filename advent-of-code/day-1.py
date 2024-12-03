#!/usr/bin/python3

import csv
import sys
import os


def get_absolute_path(file_path):
    """Converts relative file path to absolute file path."""
    return os.path.abspath(file_path)


def read_lists_from_csv(file_path):
    """Reads lists from CSV file."""
    list_a, list_b = [], []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skips header row
        for row in csv_reader:
            if row:  # Ensures row is not empty
                list_a.append(int(row[0]))  # Column 1: ListA
                list_b.append(int(row[1]))  # Column 2: ListB
    return list_a, list_b


def update_csv_with_distances(input_file_path, output_file_path):
    """Reads lists from CSV file, calculates distances & updates CSV."""
    # Step 1: Read
    list1, list2 = read_lists_from_csv(input_file_path)

    # Step 2: Sort in descending order
    list1_sorted = sorted(list1, reverse=True)
    list2_sorted = sorted(list2, reverse=True)

    # Step 3: Calculate distance btn pairs
    distances = [abs(a - b) for a, b in zip(list1_sorted, list2_sorted)]

    # Step 4: Sum distance
    total_distance = sum(distances)

    # Step 5: Write sorted lists, distances & sum distance to output CSV
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ListA (sorted)", "ListB (sorted)", "Distance"])
        for a, b, d in zip(list1_sorted, list2_sorted, distances):
            writer.writerow([a, b, d])
        writer.writerow([])  # Adds blank row
        writer.writerow(["Total Distance", total_distance])

    print(f"Results written to {output_file_path}")


def main():
    """Main function to handle command-line args & process CSV files."""
    if len(sys.argv) != 3:
        print("Usage: ./day-1.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

    input_file_path = get_absolute_path(sys.argv[1])
    output_file_path = get_absolute_path(sys.argv[2])

    update_csv_with_distances(input_file_path, output_file_path)


if __name__ == "__main__":
    main()

