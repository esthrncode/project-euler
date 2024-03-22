#brute-force approach
from time import perf_counter

def count_divisors(n: int) -> int:
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # Count both i and n // i
        if i * i == n:  # Correct for a perfect square
            count -= 1
    return count

def find_triangle_number(n_divisors):
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2  
        if count_divisors(triangle_number) > n_divisors:
            return triangle_number
        n += 1

n_divisors = 500

start_time = perf_counter()
triangle_number = find_triangle_number(n_divisors)
end_time = perf_counter()

print(triangle_number, end_time - start_time)
