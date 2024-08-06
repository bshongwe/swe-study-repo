# Problem Set

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:

$$ 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$
Your task is to simulate the execution of the algorithm for a given value of n.
Input
The only input line contains an integer n.
Output
Print a line that contains all values of n during the algorithm.
Constraints

1 \le n \le 10^6

Example
Input:
3

Output:
3 10 5 16 8 4 2 1

<br></br>
# Solution
To solve this problem, we'll simulate the described algorithm step-by-step. We'll start with an initial positive integer n and apply the following rules iteratively until n becomes 1:
-   If n is even, divide it by 2.
-   If n is odd, multiply it by 3 and add 1.

We will keep track of all values of n during this process and print them as a sequence. This code handles the problem efficiently even for the upper constraint 1 ≤ n ≤ 10^6 by ensuring each step is performed in constant time.
<br></br>

# Explanation
Function collatz_sequence(n):</br>
This function simulates the Collatz sequence starting from n.
-   It initializes an empty list sequence to store the values of n.
-   It runs a while loop until n becomes 1.
-   Inside the loop, it appends the current value of n to sequence.
-   It checks if n is even or odd and updates n accordingly:
    -   If n is even (n % 2 == 0), it divides n by 2.
    -   If n is odd, it sets n to 3 * n + 1.
    -   After the loop, it appends the final value 1 to sequence.
    -   It returns the complete sequence.

Reading Input:</br>
The input is read using input().strip() and converted to an integer n.</br>
Generating and Printing the Sequence:
-   The collatz_sequence(n) function is called to get the sequence for the input n.
-   The resulting list is converted to a string of space-separated numbers using " ".join(map(str, result)).
-   This string is printed to output the sequence.
