import time

def square_of_sum(n: int) -> int: # calculate the sum of the first n natural numbers, then square that total.
    return (n * (n + 1) // 2) ** 2

def sum_of_squares(n: int) -> int: #calculate the squares of each of the first n natural numbers and sum those squares.
    return n * (n + 1) * (2 * n + 1) // 6

def difference(n: int) -> int: #difference between these two values
    return square_of_sum(n) - sum_of_squares(n)

# first 100 natural numbers
n = 100

start_time = time.time()
print(difference(n)) #print result
print(time.time() - start_time)