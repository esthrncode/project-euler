# Solution 1
#def sumOfMultiples(maxNumber):
    #sum = 0
    #for number in range(1, maxNumber):  # number is from 1 to maxNumber-1
     #   if number % 3 == 0 or number % 5 == 0:
      #      sum += number
    #return sum
#result = sumOfMultiples(1000)

# but if we consider a time complexity of O(N) (based on Big O notation) which isn't efficient for large numbers, so I tried to make it become O(1)
# using arithmetic series formula:

#Solution 2
def arithmeticSum(a, maxNumber):
    n = (maxNumber - 1) // a #find the total number in the series
    b = a * n #find the last number in the series
    return n * (a + b) // 2 # apply the arithmetic series sum formula
    
    result = arithmeticSum(3, 1000) + arithmeticSum(5,1000) - arithmeticSum(15,1000)
    print(result)
    