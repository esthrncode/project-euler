# brute-force approach

from time import perf_counter

def find_greatest_product(number, k: int) -> int:
    digit_list = [int(digit) for digit in str(number)]
    
    max_product = 0
    
    for i in range(len(digit_list) - k + 1):
        product = 1
        for j in range(k):
            product *= digit_list[i + j]
        
        max_product = max(max_product, product)
    
    return max_product

number_str = "73167176531330624919225119674426574742355349194934"  
k = 4  

start_time = perf_counter()
print(find_greatest_product(number_str, k))
end_time = perf_counter()

print( end_time - start_time)
