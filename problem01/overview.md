# Problem 1: Multiples of 3 and 5

This note explains two  approaches to solving Problem 1 from Project Euler: finding the sum of all the multiples of 3 or 5 below 1000.

### Solution 1: Loop-Based Approach

The first approach is to use a simple loop to iterate over each number up to 1000 and accumulate the sum of numbers that are multiples of 3 or 5.

```bash
def sumOfMultiples(maxNumber):
    total_sum = 0
    for number in range(1, maxNumber):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number
    return total_sum

result = sumOfMultiples(1000)
```
This solution is straightforward but has a linear time complexity, O(N) based on ***Big O Notation**. It means the execution time will increase linearly with the input size, which can be inefficient for large values of N.
*In computer science, Big O is often used to describe the worst-case complexity of an algorithm*

* *O(N): Indicates the time it takes to run your algorithm increases linearly with the input size.*

* *O(1): Indicates the execution time is constant and does not increase with input size.*

So, to optimize the first solution and reduce the time complexity to O(1): 
### Solution 2: Using Arithmetic Series Formula
#### The Arithmetic Series Formula

The sum of an arithmetic series can be calculated using the formula:

$$ S = \frac{n}{2} \times (a_1 + a_n) $$

where:
-  $S$ is the sum of the series.
-  $n$  is the number of terms.
- $a_1$ is the first term in the series.
- $a_n$ is the last term in the series.

In problem 1, the series consists of multiples of 3, 5, and their least common multiple, 15. To avoid double-counting the multiples of 3 and 5 that are also multiples of 15, the sum of multiples of 15 is subtracted from the total.

```bash
def arithmeticSum(a, maxNumber):
    n = (maxNumber - 1) // a #find the total number in the series
    b = a * n #find the last number in the series
    return n * (a + b) // 2 # apply the arithmetic series sum formula

result = arithmeticSum(3, 1000) + arithmeticSum(5,1000) - arithmeticSum(15,1000) #avoid double-counting multiples of 15

print(result)
```
#
**Next**: problem02
