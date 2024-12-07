#!/usr/bin/python3

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


def calculate_similarity_score(input_file_path):
    """Calculates the similarity score between ListA and ListB."""
    validate_csv_headers(input_file_path)
    list_a, list_b = read_lists_from_csv(input_file_path)

    right_count = {}
    for num in list_b:
        right_count[num] = right_count.get(num, 0) + 1

    similarity_score = sum(num * right_count.get(num, 0) for num in list_a)
    logging.info(f"Similarity Score: {similarity_score}")
    return similarity_score


def print_help():
    """Prints usage instructions."""
    help_message = """
    Usage: ./day-1.py <input_file.csv> <mode> [<output_file.csv>]
    
    Description:
        Script calculates absolute distances or similarity scores based on
        input CSV files.

    Arguments:
        input_file.csv: Path of input CSV file containing 'ListA' and 'ListB'.
        mode: 'distance' for total distance, 'similarity' for similarity score.
        output_file.csv: Required if mode is 'distance'.

    Examples:
        ./day-1.py input.csv distance output.csv
        ./day-1.py input.csv similarity
    """
    print(help_message)


def main():
    """Main function to handle command-line args and process CSV files."""
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

    if len(sys.argv) not in [3, 4] or "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        sys.exit(0)

    input_file_path = get_absolute_path(sys.argv[1])
    mode = sys.argv[2].lower()

    if mode == "distance":
        if len(sys.argv) != 4:
            logging.error("Error: Missing output file path for 'distance' mode.")
            print_help()
            sys.exit(1)
        output_file_path = get_absolute_path(sys.argv[3])
        calculate_and_write_distances(input_file_path, output_file_path)

    elif mode == "similarity":
        score = calculate_similarity_score(input_file_path)
        print(f"Similarity Score: {score}")

    else:
        logging.error("Error: Invalid mode specified.")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
