#!/usr/bin/env python3

"""
Garden Groups - Calculate total cost of fencing all regions in a garden map.
Script reads CSV file containing garden map, identifies regions of same plant
type, calculates area and perimeter, and determines total fencing cost.
"""


def parse_input(file_path):
    """
    Parse garden map from a CSV file.

    Args:
        file_path (str): Path to input CSV file.

    Returns:
        list[list[str]]: 2D list representing garden map.
    """
    garden_map = []
    with open(file_path, "r") as file:
        for line in file:
            garden_map.append(list(line.strip()))
    print("Parsed Garden Map:")
    for row in garden_map:
        print(row)
    return garden_map

def flood_fill(grid, x, y, plant_type):
    """
    Perform a flood fill to find all connected cells of same plant type.

    Args:
        grid (list[list[str]]): 2D list representing garden map.
        x (int): Row index of starting cell.
        y (int): Column index of starting cell.
        plant_type (str): Type of plant to search for.

    Returns:
        tuple[int, int]: Area and perimeter of region.
    """
    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()

        if not (0 <= cx < rows and 0 <= cy < cols) or grid[cx][cy] != plant_type:
            continue

        grid[cx][cy] = None
        area += 1

        edges = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == plant_type:
                stack.append((nx, ny))
            else:
                edges += 1

        perimeter += edges

    print(f"Flood-fill found plant {plant_type} at ({x}, {y}) -> "
          f"Area: {area}, Perimeter: {perimeter}")
    return area, perimeter

def calculate_total_price(grid):
    """
    Calculate the total price of fencing all regions in the garden map.

    Args:
        grid (list[list[str]]): 2D list representing the garden map.

    Returns:
        int: Total price of fencing all regions.
    """
    total_price = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]:
                plant_type = grid[x][y]
                area, perimeter = flood_fill(grid, x, y, plant_type)
                price = area * perimeter
                print(f"Region Plant Type: {plant_type}, Area: {area}, "
                      f"Perimeter: {perimeter}, Price: {price}")
                total_price += price

    print(f"Final Total Price: {total_price}")
    return total_price

def main():
    """
    Main function to execute the script.

    Reads the input file, calculates the total fencing cost, and prints result.
    """
    file_path = 'input_file.csv'
    garden_map = parse_input(file_path)
    total_price = calculate_total_price(garden_map)
    print(f'Total price of fencing all regions: {total_price}')

if __name__ == '__main__':
    main()
