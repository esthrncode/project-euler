# brute-force approach
def is_prime(n):
    """check if a number is prime using a simple method."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# optimal approach
def find_nth_prime_optimized(n):
    if n == 1:
        return 2
    count = 1  # starting with 2 as the first prime
    num = 1
    while count < n:
        num += 2  # skip even numbers after 2
        if is_prime(num):
            count += 1
    return num

# find the 10001st prime using the brute-force method
print(find_nth_prime(10001))
      
# find the 10001st prime using the optimal method
print(find_nth_prime_optimized(10001))

