def sum_of_even_fibonacci(limit):
    a, b = 1, 2 # first two Fibonacci numbers
    sum_even = 2 # the sum = first even number

    
    while a + b <= limit:
        c = a + b # compute the next Fibonacci number
            
        if c % 2 == 0:
            sum_even += c # if 'c' is even, add it to the sum
        
        if c > limit: 
            break # break the loop if number is exceed the limit
    
    # set the next pair
        a = b
        b = c

    return sum_even

result = sum_of_even_fibonacci(4000000) 
print("Result from second method:", result)