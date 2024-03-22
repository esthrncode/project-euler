# brute-force approach

from math import factorial
from time import perf_counter
from turtle import st
def factorial(n:int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
sum = 0
n = 100
start_time = perf_counter()
print(sum([n for n in str(factorial(n))]))
end_time = perf_counter()
print(end_time - start_time)