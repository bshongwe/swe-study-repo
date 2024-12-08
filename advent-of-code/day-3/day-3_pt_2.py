#!/usr/bin/python3

import os
import re


def extract_and_compute_sum_with_controls(memory_content):
    """
    Extract valid mul(X,Y) instructions considering do() and don't() controls, 
    and compute the total sum of enabled multiplications.

    :param memory_content: String representing corrupted memory.
    :return: Sum of results from all enabled mul(X,Y) instructions.
    """
    # Regex patterns for instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"(do\(\)|don't\(\))"

    # Combine both patterns
    combined_pattern = f"{control_pattern}|{mul_pattern}"
    all_matches = re.findall(combined_pattern, memory_content)

    result_sum = 0
    mul_enabled = True  # Initially, mul instructions are enabled

    # Process matches
    for match in all_matches:
        if match[0]:  # This is a control instruction
            if match[0] == "do()":
                mul_enabled = True
            elif match[0] == "don't()":
                mul_enabled = False
        elif match[1] and match[2]:  # This is a mul(X, Y) instruction
            if mul_enabled:
                x, y = int(match[1]), int(match[2])
                result_sum += x * y

    return result_sum


def process_memory_file(file_path):
    """
    Process memory file to compute the sum of valid mul(X,Y) results with controls.

    :param file_path: Path to memory file.
    :return: Sum of results from all valid and enabled mul(X,Y) instructions.
    """
    try:
        with open(file_path, "r") as file:
            corrupted_memory = file.read()
            return extract_and_compute_sum_with_controls(corrupted_memory)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def main():
    """Main function to run corrupted memory analysis with controls."""
    # Dynamically determine the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input_file.csv")

    # Resolve and process file
    print("Starting corrupted memory analysis...")
    result_sum = process_memory_file(file_path)
    print(f"Total sum of valid and enabled multiplications: {result_sum}")


if __name__ == "__main__":
    main()
