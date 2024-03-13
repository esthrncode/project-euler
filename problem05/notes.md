# Project Euler Problem 5: Smallest Multiple Explained

#### Understanding the Problem

The objective is to identify a number that can be divided evenly (no remainder) by all numbers from 1 to 20. It's a practical demonstration of finding the LCM in computational problem-solving.

#### The Concept of Least Common Multiple (LCM)

The LCM is the smallest number that is a multiple of two or more integers. The formula for calculating the LCM of two integers, `a` and `b`, utilizing their Greatest Common Divisor (GCD), is as follows:

```plaintext
LCM(a, b) = |a * b| / GCD(a, b)
```
In Python there is a library for GCD, 
```python
from math import gcd
```
so we dont need to write the fomular for GCD in our code. But if you want to, here is the code for GCD:
```bash
def gcd(a: int, b: int) -> int:
    r = b % a 
    while r > 0:
        b = a
        a = r 
        r = b % a 
    return a 
```
#### Performanve Measurement
We can measure the code run time by 
```bash
import time

start_time = time.time()
print(f"The smallest multiple is: {smallest_multiple(20)}")
print(f"Execution time: {time.time() - start_time} seconds")
``` 
