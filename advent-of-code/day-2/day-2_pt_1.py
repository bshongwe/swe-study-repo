#!/usr/bin/python3

import os


def is_safe_report(report):
    """Check if a report is safe based on the given conditions."""
    levels = list(map(int, report.strip().split()))
    
    # Checks for difference condition (between 1 and 3)
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])
        if diff < 1 or diff > 3:
            return False
    
    
    # Checks if list is strictly increasing or strictly decreasing
    increasing = True
    decreasing = True
    for i in range(1, len(levels)):
        if levels[i] > levels[i - 1]:
            decreasing = False
        if levels[i] < levels[i - 1]:
            increasing = False
    
    # Return true
    return increasing or decreasing


def count_safe_reports(file_path):
    """Counts number of safe reports in file."""
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            if is_safe_report(line):
                safe_count += 1
    return safe_count


def main():
    """Main function to run the report safety analysis."""
    # Path to the input file
    file_path = r"input_file.csv"
    
    # Resolves absolute path and checks existence
    file_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        exit(1)
    
    # Calculates and prints number of safe reports
    try:
        result = count_safe_reports(file_path)
        print(f"Number of safe reports: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()