# Project Euler Problem 7: Finding the 10001st Prime Number

### Understanding the Problem
Find the 10001st prime number. Prime numbers are  mathematical entities that are greater than 1 and have no divisors other than 1 and themselves. 

### Mathematical Insight

To efficiently solve this problem, we utilize some fundamental properties of prime numbers:

- **Prime Checking**: A number `n` is prime if it isn't divisible by any number less than `n` and greater than 1. However, we only need to check divisibility up to the square root of `n`, as any factors larger than the square root would have corresponding factors smaller than the square root.

- **Skipping Even Numbers**: Except for 2, all prime numbers are odd. So, after checking 2, we can skip all even numbers to speed up our search.

