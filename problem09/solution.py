# brute-force approach

import time

def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a, target_sum // 2):
            c = target_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None

target_sum = 1000
triplet = find_pythagorean_triplet(target_sum)

if triplet:
    a, b, c = triplet
    print(a*b*c)
else:
    print("No Pythagorean triplet found")

