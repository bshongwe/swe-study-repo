#!/usr/bin/env python3
import os
import csv


def get_absolute_path(filename):
    """Returns the absolute path to the file in the current working directory."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def read_equations(file_path):
    """Reads the CSV file and returns a list of equations."""
    equations = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Split the row at the first colon and strip excess spaces
            target, numbers_str = row[0].strip().split(":")
            target = int(target.strip())
            numbers = list(map(int, numbers_str.strip().split()))
            equations.append((target, numbers))
    return equations


def evaluate_with_pruning(numbers, target, current_value, index):
    """Recursively evaluates the equation with pruning based on target."""
    if index == len(numbers):
        return current_value == target

    # Pruning condition: stop if current value cannot logically lead to target
    if current_value > target:
        return False

    # Try addition
    if evaluate_with_pruning(numbers, target, current_value + numbers[index], index + 1):
        return True

    # Try multiplication
    if evaluate_with_pruning(numbers, target, current_value * numbers[index], index + 1):
        return True

    # Try concatenation (||)
    concatenated_value = int(str(current_value) + str(numbers[index]))
    if evaluate_with_pruning(numbers, target, concatenated_value, index + 1):
        return True

    return False


def evaluate_equation(target, numbers):
    """Evaluates a single equation by checking if it can be valid."""
    return evaluate_with_pruning(numbers, target, numbers[0], 1)


def calculate_total_calibration_result(equations):
    """Calculates the total calibration result for all valid equations."""
    total_calibration_result = 0
    valid_equations = 0

    for target, numbers in equations:
        if evaluate_equation(target, numbers):
            total_calibration_result += target
            valid_equations += 1

    return total_calibration_result, valid_equations


def evaluate_part1(equations):
    """Solves Part 1: Valid equations using only addition and multiplication."""
    total_calibration_result = 0
    valid_equations = 0

    for target, numbers in equations:
        # Evaluate only using addition and multiplication, no concatenation
        if evaluate_equation(target, numbers):
            total_calibration_result += target
            valid_equations += 1

    return total_calibration_result, valid_equations


def main():
    file_path = get_absolute_path("input_file.csv")
    equations = read_equations(file_path)

    # Part 1: Valid equations using only + and *
    part1_result, part1_valid_equations = evaluate_part1(equations)
    print(f"Part 1: Total Calibration Result = {part1_result}")
    print(f"Part 1: Valid Equations = {part1_valid_equations}")

    # Part 2: Valid equations using +, *, and || (concatenation)
    part2_result, part2_valid_equations = calculate_total_calibration_result(equations)
    print(f"Part 2: Total Calibration Result = {part2_result}")
    print(f"Part 2: Valid Equations = {part2_valid_equations}")


if __name__ == "__main__":
    main()
