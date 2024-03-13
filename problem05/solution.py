import time
from math import gcd 

# brute-force approach
def is_divisible(number):
    # checks if 'number' is divisible by all numbers from 1 to 20
    for divisor in range(1, 21):
        if number % divisor != 0:
            return False
    return True

def smallest_multiple_brute_force():
    number = 1
    while True:
        if is_divisible(number): # check if the current number meets our criteria
            return number
        number += 1

# optimized approach using LCM

def lcm(a, b):
    # calculate the least common multiple (LCM) using the greatest common divisor (GCD)
    return a * b // gcd(a, b)

def smallest_multiple_optimized(n):
    smallest_mult = 1
    for i in range(2, n + 1): # loop through numbers 2 to n
        smallest_mult = lcm(smallest_mult, i) # update 'smallest_mult' with the LCM of itself and the current number 'i'
    return smallest_mult

# measure and print runtime of the optimized approach
start_time = time.time()

print(smallest_multiple_optimized(20))
print(time.time() - start_time)

# Note: the brute-force approach is commented out due to its long runtime.