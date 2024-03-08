# Solution 1 by using loop
def sumOfMultiples(maxNumber):
    sum = 0
    for number in range(1, maxNumber):  # number is from 1 to maxNumber-1
       if number % 3 == 0 or number % 5 == 0:
           sum += number
    return sum

# but if we consider a time complexity of O(N) (based on Big O notation) which isn't efficient for large numbers, so I tried to make it become O(1)

#Solution 2 by using arithmetic series formula

def arithmeticSum(a, maxNumber):
    n = (maxNumber - 1) // a #find the total number in the series
    b = a * n #find the last number in the series
    return n * (a + b) // 2 # apply the arithmetic series sum formula

# Main block to control which solution is executed
if __name__ == "__main__":
    maxLimit = 1000
    
    # Run Solution 1
    print("Solution 1 Result:", sumOfMultiples(1000))
    
    # Run Solution 2
    optimizedResult = arithmeticSum(3, 1000) + arithmeticSum(5,1000) - arithmeticSum(15,1000) #avoid double-counting multiples of 15
    print("Solution 2 Result:", optimizedResult)

