# import math
# def is_prime(n: int)-> bool:
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_primes(limit: int)-> int:
#     return sum([i for i in range(2, limit) if is_prime(i)])

import math

def is_prime(n: int) -> bool:  # Corrected return type annotation to bool
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Correctly includes math.sqrt(n) + 1
        if n % i == 0:
            return False
    return True

def sum_primes(limit: int) -> int:
    return sum(i for i in range(2, limit) if is_prime(i))  # Used a generator expression for memory efficiency
