def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    sequence.append(1)  # Finally append the last number, which is 1
    return sequence

# Read input
n = int(input().strip())

# Get the sequence
result = collatz_sequence(n)

# Print the sequence
print(" ".join(map(str, result)))
