#!/usr/bin/env python3

import csv
import os
from itertools import product


def read_equations(file_path):
    """Reads equations from a CSV file and returns them as a list."""
    equations = []
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            target = int(row[0])
            numbers = list(map(int, row[1].strip().split()))
            equations.append((target, numbers))
    return equations


def evaluate_expression(numbers, operators):
    """
    Evaluate expression left-to-right using numbers and operators.

    :param numbers: List of integers.
    :param operators: List of operators ('+' or '*').
    :return: Result of the evaluation.
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result


def find_valid_equations(equations):
    """
    Determines which equations can be made valid and calculates the total result.

    :param equations: List of tuples with target and numbers.
    :return: Tuple (total result, list of valid equations).
    """
    total_result = 0
    valid_equations = []

    for target, numbers in equations:
        num_operators = len(numbers) - 1
        valid = False

        # Generate all possible combinations of operators
        for operators in product("+-*", repeat=num_operators):
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break

        if valid:
            total_result += target
            valid_equations.append((target, numbers))

    return total_result, valid_equations


if __name__ == "__main__":
    # Absolute path to the input CSV file
    file_path = os.path.abspath("input_file.csv")

    # Read equations from the CSV file
    equations = read_equations(file_path)

    # Valid equations + total calibration result
    total_calibration_result, valid_equations = find_valid_equations(equations)

    # Output results
    print(f"Part 1: Total Calibration Result = {total_calibration_result}")
    print(f"Part 1: Valid Equations = {len(valid_equations)}")
