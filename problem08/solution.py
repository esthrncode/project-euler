# brute-force approach

from time import perf_counter

def find_greatest_product(number_str, k: int)-> int:
    digit_list = [int(digit) for digit in str(number_str)]
    max_product = 0
    for i in range(len(digit_list) - k + 1):
        product = 1
        for j in range(k):
            product *= digit_list[i + j]
        max_product = max(max_product, product)
    return max_product

# optimal approach

def find_greatest_product_optimal(number_str, k: int)-> int:
    digit_list = [int(digit) for digit in str(number_str)]
    max_product = 0
    zero_index = -1
    for i in range(len(digit_list) - k + 1):
        if i <= zero_index:
            continue
        product = 1
        for j in range(i, i + k):
            if digit_list[j] == 0:
                zero_index = j
                break
            product *= digit_list[j]
        else:
            max_product = max(max_product, product)
    return max_product

number_str = "73167176531330624919225119674426574742355349194934" 
k = 13 

start_time = perf_counter()
result_brute_force = find_greatest_product(number_str, k)
end_time = perf_counter()
print(result_brute_force)
print(end_time - start_time)

start_time = perf_counter()
result_optimal = find_greatest_product_optimal(number_str, k)
end_time = perf_counter()
print(result_optimal)
print(end_time - start_time)
