# brute-force approach

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0  # Count of prime numbers found
    num = 1 
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Find the 10001st prime number
print(nth_prime(10001))

#optimal approach
