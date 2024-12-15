#!/usr/bin/env python3

import csv
import sys
from sympy import symbols, Eq, diophantine


def parse_input(file_path):
    """Parse CSV file to extract machine configs."""
    machines = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 7:
                continue
            Ax, Ay = int(row[0]), int(row[1])
            Bx, By = int(row[2]), int(row[3])
            Px, Py = int(row[4]), int(row[5])
            machines.append(((Ax, Ay), (Bx, By), (Px, Py)))
    return machines


def find_min_cost(Ax, Ay, Bx, By, Px, Py):
    """Solve equations to find minimum cost."""
    x, y = symbols("x y", integer=True)

    # Define equations
    eq_x = Eq(Ax * x + Bx * y, Px)
    eq_y = Eq(Ay * x + By * y, Py)

    # Solve equations for x and y
    solutions_x = diophantine(eq_x)
    solutions_y = diophantine(eq_y)

    # Match solutions for valid (x, y) pairs
    valid_solutions = []
    for sx in solutions_x:
        for sy in solutions_y:
            if sx == sy and sx[0] >= 0 and sx[1] >= 0:
                valid_solutions.append(sx)

    if not valid_solutions:
        return float("inf"), None

    # Calculate cost for each valid solution
    min_cost = float("inf")
    best_solution = None
    for sol in valid_solutions:
        cost = 3 * sol[0] + sol[1]
        if cost < min_cost:
            min_cost = cost
            best_solution = sol

    return min_cost, best_solution


def main():
    # Read file path from command-line arg
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input_file.csv"
    machines = parse_input(input_file)

    total_cost = 0
    prizes_won = 0

    for i, machine in enumerate(machines):
        (Ax, Ay), (Bx, By), (Px, Py) = machine
        cost, solution = find_min_cost(Ax, Ay, Bx, By, Px, Py)
        if cost != float("inf"):
            prizes_won += 1
            total_cost += cost
            print(f"Machine {i + 1}: Solution = {solution}, Cost = {cost}")
        else:
            print(f"Machine {i + 1}: No solution")

    print(f"Total Prizes Won: {prizes_won}")
    print(f"Minimum Total Cost: {total_cost}")


if __name__ == "__main__":
    main()
