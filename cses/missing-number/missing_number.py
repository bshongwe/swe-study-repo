def find_missing_number(n, numbers):
    sum_n = n * (n + 1) // 2
    sum_given = sum(numbers)
    missing_number = sum_n - sum_given
    return missing_number

# Read input
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# Find and print the missing number
missing_number = find_missing_number(n, numbers)
print(missing_number)
