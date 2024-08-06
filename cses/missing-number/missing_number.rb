def find_missing_number(n, numbers)
  sum_n = n * (n + 1) / 2
  sum_given = numbers.sum
  missing_number = sum_n - sum_given
  missing_number
end

# Read input
input = $stdin.read.split.map(&:to_i)

# The first input line contains an integer n
n = input[0]

# The second line contains n-1 numbers
numbers = input[1..-1]

# Find and print the missing number
missing_number = find_missing_number(n, numbers)
puts missing_number
