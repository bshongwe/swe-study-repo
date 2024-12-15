#!/usr/bin/env python3

import os

def calculate_total_distance(file_path):
    with open(file_path, "r") as file:
        pairs = [tuple(map(int, line.strip().split())) for line in file]
    
    left_list = sorted(pair[0] for pair in pairs)
    right_list = sorted(pair[1] for pair in pairs)
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    return total_distance

# Path to the input file
file_path = r"input_file.csv"

# Debugging: Print current directory and contents
print(f"Current working directory: {os.getcwd()}")
print(f"Files in directory: {os.listdir()}")

# Resolve and check path
file_path = os.path.abspath(file_path)
print(f"Resolved absolute file path: {file_path}")

if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    exit(1)

try:
    print(f"Total distance: {calculate_total_distance(file_path)}")
except Exception as e:
    print(f"An error occurred: {e}")
