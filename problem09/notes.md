# Solving Project Euler Problem 9: A Special Pythagorean Triplet

### Understanding the Problem

We need to find a specific set of three numbers, known as a Pythagorean triplet, where:

- Each of the numbers is a positive integer.
- They fit the rule `a^2 + b^2 = c^2`
- They add up to 1000: `a + b + c = 1000`.
  
It ask us to find the product `abc`

### Strategy for Solving the Problem

1. **Fixed Sum**: We know that `a + b + c = 1000`. We can narrow down possible values of `a`, `b`, and `c`.

2. **Iterative Search**: Because `a`, `b`, and `c` are positive integers with `a < b < c`, we can iterate through possible values of `a` and `b` to find a corresponding `c` that meets both conditions.

3. **Optimization**: Realize that `c = 1000 - a - b`. This means we don't need to iterate for `c`, significantly reducing the number of iterations.

4. **Stop Condition**: Since `a < b < c` and their sum is 1000, `a` can be at most 332 (because `333 + 334 + 335 > 1000`), and `b` must be less than `c`, giving us range for both `a` and `b`.




