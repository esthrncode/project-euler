# brute-force approach

from math import factorial
from time import perf_counter

def factorial_digit_sum(n:int) -> int:
    factor_digit = factorial(n)
    sum_digits = 0

    for digit in str(factor_digit):
        sum_digits += int(digit)
    return sum_digits

n = 100
start_time = perf_counter()
print(factorial_digit_sum(n)) 
end_time = perf_counter()
print(end_time - start_time)