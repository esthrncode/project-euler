#Solution 2 by using arithmetic series formula

def arithmeticSum(a, maxNumber):
    n = (maxNumber - 1) // a #find the total number in the series
    b = a * n #find the last number in the series
    return n * (a + b) // 2 # apply the arithmetic series sum formula

result = arithmeticSum(3, 1000) + arithmeticSum(5,1000) - arithmeticSum(15,1000) #avoid double-counting multiples of 15

print(result)