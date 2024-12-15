#!/usr/bin/env python3

import os

def calculate_total_distance(file_path):
    with open(file_path, "r") as file:
        pairs = [tuple(map(int, line.strip().split())) for line in file]
    
    left_list = sorted(pair[0] for pair in pairs)
    right_list = sorted(pair[1] for pair in pairs)
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    
    return total_distance


def calculate_similarity_score(file_path):
    with open(file_path, "r") as file:
        left_list = []
        right_list = []
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences in right_list
    right_count = {}
    for num in right_list:
        right_count[num] = right_count.get(num, 0) + 1

    # Calculate similarity score
    similarity_score = sum(num * right_count.get(num, 0) for num in left_list)
    
    return similarity_score


# Path to the input file
file_path = r"input_file.csv"

# Resolve to absolute path and check existence
file_path = os.path.abspath(file_path)
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    exit(1)

# Prompt for mode
mode = input("Enter mode ('distance' for total distance, 'similarity' for similarity score): ").strip().lower()

try:
    if mode == "distance":
        result = calculate_total_distance(file_path)
        print(f"Total distance: {result}")
    elif mode == "similarity":
        result = calculate_similarity_score(file_path)
        print(f"Similarity score: {result}")
    else:
        print("Error: Invalid mode. Please choose 'distance' or 'similarity'.")
except Exception as e:
    print(f"An error occurred: {e}")
