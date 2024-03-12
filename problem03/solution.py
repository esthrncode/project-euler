# Solution 1

def largest_prime_factor(n):
    i = 2 # smallest prime factor
    
    # if we want to find the largest prime factor of a number n, you only need to check numbers from 2 up to the "square root of n".
    while i * i <= n: 
        if n % i: # if n is not divisible by i
            i += 1 # try next number
        else:
            n //= i
    return n

# Solution 2

def largest_prime_factor_optimized(n):

    while n % 2 == 0:  # remove all factors of 2, since 2 is the only even prime number
        n = n // 2
        largest_factor = 2

    factor = 3     # check odd numbers starting from 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n = n // factor
        factor += 2  # Increment by 2 to check only odd numbers
        
    if n > 2:
        largest_factor = n
    return largest_factor

number = 600851475143
print(largest_prime_factor(number))
print(largest_prime_factor_optimized(number))
