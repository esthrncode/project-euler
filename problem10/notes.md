# Solving Project Euler Problem 10: Prime Summation

### Understanding the Problem

Find the sum of all the prime numbers below two million. This problem requires an algorithm to compute the sum due to the high limit.

### Strategy for Solving the Problem

Using Sieve of Eratosthenes, an ancient algorithm for finding all prime numbers up to any given limit: 

1. **Create a List**: Start with a list of boolean values,numbers starting from 0 up to the limit. All numbers are potentially prime.

2. **Eliminate Non-Primes**: Begin with the first prime number, 2. Eliminate all multiples of 2, since they cannot be prime. Repeat this process for the next number in the list that has not been eliminated. This step is repeated for all numbers up to the square root of the limit.

3. **Sum the Primes**: After all multiples of each found prime are eliminated, the remaining numbers marked as potentially prime are indeed prime. Then sum these prime numbers.
