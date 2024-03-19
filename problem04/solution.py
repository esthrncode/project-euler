from timeit import default_timer as timer

def is_palindrome(n):
    return str(n) == str(n)[::-1] # cooanverts n to string and compares n to its palindrome

def find_largest_palindrome():
    largest_palindrome = 0
    for i in range(999, 99, -1): # loop from 999 down to 100 with decrement of 1
        for j in range(i, 99, -1): # loop from i down to 100 with decrement of 1, to avoid redundant checks
            product = i * j
            if product <= largest_palindrome:
                break # since we aim to found the largest palindrome and j is decreasing, further products will be smaller, 
            if is_palindrome(product):
                largest_palindrome = product
                break
    return largest_palindrome
print(find_largest_palindrome())

start = timer() 
end = timer()
print(end - start)