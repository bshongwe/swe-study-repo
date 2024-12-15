#!/usr/bin/env python3

import csv
import sys
import os
import logging


def get_absolute_path(file_path):
    """Converts relative file path to absolute file path."""
    abs_path = os.path.abspath(file_path)
    logging.debug(f"Converted {file_path} to absolute path: {abs_path}")
    return abs_path


def validate_csv_headers(file_path):
    """Validates input CSV file contains correct headers."""
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            if not headers or headers[:2] != ["ListA", "ListB"]:
                logging.error(f"Error: Missing or invalid headers in {file_path}. Found headers: {headers}")
                sys.exit(1)
            logging.debug(f"Headers validated successfully: {headers}")
    except Exception as e:
        logging.error(f"Error while validating headers: {e}")
        sys.exit(1)


def read_lists_from_csv(file_path):
    """Reads two lists of integers from CSV file."""
    list_a, list_b = [], []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skips header row <ListA,ListB part>
            for row in csv_reader:
                if row:  # Ensures row is not empty
                    try:
                        list_a.append(int(row[0]))  # Column 1: ListA
                        list_b.append(int(row[1]))  # Column 2: ListB
                        logging.debug(f"Added row: {row}")
                    except ValueError as e:
                        logging.error(f"Error: Non-integer value in row {row}. Exception: {e}")
                        sys.exit(1)
    except FileNotFoundError:
        logging.error(f"Error: File {file_path} does not exist.")
        sys.exit(1)
    except PermissionError:
        logging.error(f"Error: Permission denied to read the file {file_path}.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error while reading the file: {e}")
        sys.exit(1)

    return list_a, list_b


def calculate_and_write_distances(input_file_path, output_file_path):
    """Calculates ListA & ListB distances, prints result in output_file.csv."""
    validate_csv_headers(input_file_path)
    list_a, list_b = read_lists_from_csv(input_file_path)

    if not list_a or not list_b:
        logging.error("Error: One or both lists are empty.")
        sys.exit(1)

    if len(list_a) != len(list_b):
        logging.error("Error: Mismatched list lengths. ListA: {len(list_a)}, ListB: {len(list_b)}")
        sys.exit(1)

    list_a_sorted = sorted(list_a)
    list_b_sorted = sorted(list_b)
    logging.debug(f"Sorted ListA: {list_a_sorted}")
    logging.debug(f"Sorted ListB: {list_b_sorted}")

    try:
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ListA (sorted)", "ListB (sorted)", "Distance"])

            total_distance = 0
            for a, b in zip(list_a_sorted, list_b_sorted):
                distance = abs(a - b)
                total_distance += distance
                logging.debug(f"Calculated distance: {distance} between {a} and {b}")
                writer.writerow([a, b, distance])

            writer.writerow([])  # Blank row before result
            writer.writerow(["Total Distance", total_distance])

        logging.info(f"Results written to {output_file_path}")
        logging.info(f"Total Distance: {total_distance}")
    except PermissionError:
        logging.error(f"Error: Permission denied to write to the file {output_file_path}.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error: An unexpected error occurred while writing to the file: {e}")
        sys.exit(1)


def print_help():
    """Prints usage instructions."""
    help_message = """
    Usage: ./day-1.py <input_file.csv> <output_file.csv>
    
    Description:
        Script calculates absolute distances between ListA & ListB, reads from
        input CSV file and writes the results to output CSV file.
    
    Arguments:
        input_file.csv: Path of input CSV file containing 'ListA' and 'ListB'.
        output_file.csv: Path of output CSV file to save the results.
    """
    print(help_message)


def main():
    """Main function to handle command-line args and process CSV files."""
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

    if len(sys.argv) != 3 or "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        sys.exit(0)

    input_file_path = get_absolute_path(sys.argv[1])
    output_file_path = get_absolute_path(sys.argv[2])

    logging.info(f"Input file: {input_file_path}")
    logging.info(f"Output file: {output_file_path}")

    calculate_and_write_distances(input_file_path, output_file_path)


if __name__ == "__main__":
    main()
