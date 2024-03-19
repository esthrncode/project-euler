# brute-force approach
import time
import math
from tracemalloc import start
def is_prime(n: int)-> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(limit: int)-> int:
    return sum([i for i in range(2, limit) if is_prime(i)])
start = time.time()
print(sum_primes(2000000))
end = time.time()
print("Time:", end - start)