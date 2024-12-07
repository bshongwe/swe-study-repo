#!/usr/bin/python3


def calculate_total_distance(file_path):
    with open(file_path, "r") as file:
        # Read and process the data in one step
        pairs = [tuple(map(int, line.strip().split())) for line in file]
    
    # Separate and sort lists directly from the parsed pairs
    left_list = sorted(pair[0] for pair in pairs)
    right_list = sorted(pair[1] for pair in pairs)

    # Calculate total distance using a generator expression
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))

    return total_distance


# Path to the input file
file_path = "advent-of-code\day-1\problem-set-2\input_file.csv"

# Calculate and print the result
print(calculate_total_distance(file_path))