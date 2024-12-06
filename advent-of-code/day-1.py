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
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skips header row
            for row in csv_reader:
                if row:  # Ensures row is not empty
                    try:
                        list_a.append(int(row[0]))  # Column 1: ListA
                        list_b.append(int(row[1]))  # Column 2: ListB
                    except ValueError:
                        print(f"Error: Non-integer value encountered in CSV row: {row}")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read the file {file_path}.")
        sys.exit(1)
    
    return list_a, list_b


def update_csv_with_distances(input_file_path, output_file_path):
    """Reads lists from CSV file, calculates distances & updates CSV."""
    # Step 1: Read
    list1, list2 = read_lists_from_csv(input_file_path)

    # Step 2: Sort in descending order
    list1_sorted = sorted(list1, reverse=True)
    list2_sorted = sorted(list2, reverse=True)

    # Debugging: Print sorted lists to check order
    print("Sorted List A:", list1_sorted)
    print("Sorted List B:", list2_sorted)

    # Step 3: Write sorted lists, distances & sum distance to output CSV
    try:
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ListA (sorted)", "ListB (sorted)", "Distance"])

            # Calculate distance and write row-by-row to avoid large memory usage
            total_distance = 0
            for a, b in zip(list1_sorted, list2_sorted):
                distance = abs(a - b)
                total_distance += distance

                # Debugging: Print individual distances
                print(f"Distance between {a} and {b} is {distance}")

                writer.writerow([a, b, distance])

            # Debugging: Print total distance
            print(f"Total Distance: {total_distance}")

            # Write total distance
            writer.writerow([])  # Adds blank row
            writer.writerow(["Total Distance", total_distance])

        print(f"Results written to {output_file_path}")
    except PermissionError:
        print(f"Error: Permission denied to write to the file {output_file_path}.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


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
