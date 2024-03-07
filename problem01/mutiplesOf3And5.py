# My first try
def sumOfMultiples(maxNumber):
    sum = 0
    for number in range(1, maxNumber):  # number is from 1 to maxNumber-1
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum

result = sumOfMultiples(1000)
print(result)
