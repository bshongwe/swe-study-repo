import sys

def find_missing_number(n, numbers):
    sum_n = n * (n + 1) // 2
    sum_given = sum(numbers)
    missing_number = sum_n - sum_given
    return missing_number

# Read input
input = sys.stdin.read
data = input().split()

# The first input line contains an integer n
n = int(data[0])

# The second line contains n-1 numbers
numbers = list(map(int, data[1:]))

# Find and print the missing number
missing_number = find_missing_number(n, numbers)
print(missing_number)
