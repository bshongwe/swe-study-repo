#!/usr/bin/env python3

import os
import re


def extract_and_compute_sum(memory_content):
    """
    Extract valid mul(X,Y) instructions and compute their total sum.

    :param memory_content: String representing corrupted memory.
    :return: Sum of results from all valid mul(X,Y) instructions.
    """
    # Regex pattern for valid mul instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory_content)
    return sum(int(x) * int(y) for x, y in matches)


def process_memory_file(file_path):
    """
    Process memory file to compute sum of valid mul(X,Y) results.

    :param file_path: Path to memory file.
    :return: Sum of results from all valid mul(X,Y) instructions.
    """
    try:
        with open(file_path, "r") as file:
            corrupted_memory = file.read()
            return extract_and_compute_sum(corrupted_memory)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def main():
    """Main function to run corrupted memory analysis."""
    # Dynamically determine the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input_file.csv")

    # Resolve and process file
    print("Starting corrupted memory analysis...")
    result_sum = process_memory_file(file_path)
    print(f"Total sum of valid multiplications: {result_sum}")


if __name__ == "__main__":
    main()
