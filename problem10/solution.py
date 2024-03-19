# brute-force approach
import time
import math
def is_prime(n: int)-> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(limit: int)-> int:
    return sum([i for i in range(2, limit) if is_prime(i)])
# start = time.time()
# print(sum_primes(2000000)) '''not recommended'''
# end = time.time()
# print("Time:", end - start)

# optimal approach: ussing sieve of eratosthenes
def sum_primes_optimal(limit: int)-> int:
    primes = [True] * limit
    primes[0], primes[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False
    return sum([i for i in range(limit) if primes[i]])
start = time.time()
print(sum_primes_optimal(2000000))
end = time.time()
print("Time:", end - start)

