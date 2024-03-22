# brute-force approach
from time import perf_counter
def sum_of_digits(n: int) -> int:
    power = 2 ** n
    power_str = str(power)
    return sum([int(digit) for digit in power_str])

n = 1000
start_time = perf_counter()
print(sum_of_digits(n)) 
end_time = perf_counter()
print(end_time - start_time)


    