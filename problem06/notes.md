# Project Euler Problem 6: Sum Square Difference

####  Understanding the Problem

We're asked to find the difference between the square of the sum and the sum of the squares of the first `n` natural numbers. 

Calculate the difference between:
1. The square of the sum of the first `n` natural numbers.
2. The sum of the squares of the first `n` natural numbers.

For `n = 100`, what is this difference?

#### Mathematical Insight

The brute-force approach would involve iterating through each number to calculate the sums and their squares. However, mathematics offers us a more elegant solution:

- **Square of the Sum**:
$$ (\sum_{i=1}^{n} i)^2 = (\frac{n(n+1)}{2})^2 $$

- **Sum of the Squares**:
  $$ \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} $$

These formulas allow us to directly compute the required values without explicit iteration.
```bash
def sum_square_difference(n):
    square_of_sum = (n * (n + 1) // 2) ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return square_of_sum - sum_of_squares

# Example for n = 100
print(sum_square_difference(100))
``` 
#### Complexity Analysis - Big(O) notation
Using direct mathematical formulas make  the solution's time complexity is O(1) — constant time. 