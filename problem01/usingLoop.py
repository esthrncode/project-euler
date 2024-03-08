# Solution 1 by using loop
def sumOfMultiples(maxNumber):
    sum = 0
    for number in range(1, maxNumber):  # number is from 1 to maxNumber-1
       if number % 3 == 0 or number % 5 == 0:
           sum += number
    return sum
result = sumOfMultiples(1000)

# but if we consider a time complexity of O(N) (based on Big O notation) which isn't efficient for large numbers, so I tried to make it become O(1)
# using arithmetic series formula -> see solution 2: usingArithmeric