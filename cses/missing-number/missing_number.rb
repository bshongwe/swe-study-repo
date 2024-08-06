def collatz_sequence(n)
  sequence = []
  while n != 1
    sequence << n
    if n.even?
      n /= 2
    else
      n = n * 3 + 1
    end
  end
  sequence << 1 # Finally append the last number, which is 1
  sequence
end

# Read input
n = gets.strip.to_i

# Get the sequence
result = collatz_sequence(n)

# Print the sequence
puts result.join(" ")
