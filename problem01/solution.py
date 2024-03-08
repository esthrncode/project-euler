# Solution 1 by using loop
def sum_of_multiples(max_number):
    sum = 0
    for number in range(1, max_number):  # number is from 1 to max_number-1
       if number % 3 == 0 or number % 5 == 0:
           sum += number
    return sum

# but if we consider a time complexity of O(N) (based on Big O notation) which isn't efficient for large numbers, so I tried to make it become O(1)

#Solution 2 by using arithmetic series formula

def arithmetic_sum(a, max_number):
    n = (max_number - 1) // a #find the total number in the series
    b = a * n #find the last number in the series
    return n * (a + b) // 2 # apply the arithmetic series sum formula

# Main block to control which solution is executed
if __name__ == "__main__":
    max_limit = 1000
    
    # Run Solution 1
    print("Solution 1 Result:", sum_of_multiples(1000))
    
    # Run Solution 2
    optimized_result = arithmetic_sum(3, 1000) + arithmetic_sum(5,1000) - arithmetic_sum(15,1000) #avoid double-counting multiples of 15
    print("Solution 2 Result:", optimized_result)

