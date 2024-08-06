# Missing Number
You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.
Constraints

2 \le n \le 2 \cdot 10^5

Example
Input:
5
2 3 1 5

Output:
4
<br></br>

# Solution
To solve this problem, we need to find the missing number in a sequence of integers from 1 to `n`, where exactly one number is missing. Given the constraints, we need an efficient solution that operates in linear time complexity O(n) and uses constant space O(1).

Here’s a step-by-step approach to solve the problem:

1. **Calculate the Sum of First `n` Numbers**: The sum of the first `n` natural numbers is given by the formula \( \text{sum\_n} = \frac{n \times (n + 1)}{2} \).

2. **Compute the Sum of Given Numbers**: Iterate through the provided list of `n-1` numbers and calculate their total sum, `sum_given`.

3. **Determine the Missing Number**: The missing number can be found by subtracting `sum_given` from `sum_n`. This is because `sum_n` should include all numbers from 1 to `n`, and the difference between `sum_n` and `sum_given` will be the missing number.

### Explanation:
- **Function `find_missing_number`**:
  - It takes `n` (total numbers expected) and `numbers` (list of `n-1` integers).
  - Calculates `sum_n`, the sum of the first `n` natural numbers using the formula \( \text{sum\_n} = \frac{n \times (n + 1)}{2} \).
  - Computes `sum_given`, the sum of the provided numbers.
  - Determines the missing number by subtracting `sum_given` from `sum_n` and returns it.

- **Reading Input**:
  - The first input line is read to get `n`.
  - The second line is read and split into a list of integers representing the `n-1` numbers.

- **Output**:
  - Computes and prints the missing number using the `find_missing_number` function.

<br></br>
# Previous commit runtime errors
I think I selected Python 2 during submission, hence the runtime errors. Nonetheless, the next commit has an enhanced approach.
-   reads `n`
-   then reads the next `n-1` numbers as a list.

### Explanation of Changes:
1. **Reading Input Correctly**:
   - We use `sys.stdin.read` to read all input at once and then split it into a list of strings.
   - The first element of the list is `n`.
   - The remaining elements are the `n-1` numbers.

2. **Handling Input and Computation**:
   - Convert the first element to integer `n`.
   - Convert the remaining elements to integers and store them in the list `numbers`.
   - Compute the missing number using the same logic as before.
   - Print the result.

This approach ensures that we handle input correctly in environments where the input is provided programmatically, avoiding attribute errors related to `strip`.
