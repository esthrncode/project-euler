# brute-force approach
from time import perf_counter
def collatz_sequence(n: int) -> int:
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        length += 1
    return length 

def longest_collatz_sequence(limit: int) -> int:
    longest_length = 0
    number = 0

    for i in range(1, limit):
        current_length = collatz_sequence(i)
        if current_length > longest_length:
            longest_length = current_length
            number = i
    
    return number, longest_length

start_time = perf_counter()
print(longest_collatz_sequence(1000000))
end_time = perf_counter()
print(end_time - start_time)