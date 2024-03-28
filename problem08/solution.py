# from time import perf_counter

# # brute-force approach

# def find_greatest_product(number_str, k: int) -> int:
#     clean_str = number_str.replace(" ", "") # remove spaces
#     clean_str = clean_str.replace("\n", "") # remove newlines
#     max_product = 0
        
#     for i in range(len(clean_str) - k + 1):
#         product = 1
#         for j in range(k):
#             product *= int(clean_str[i + j]) # convert to int before multiplying
        
#         max_product = max(max_product, product)
    
#     return max_product
# k = 13
# number_str = """73167176531330624919225119674426574742355349194934
#             96983520312774506326239578318016984801869478851843
#             85861560789112949495459501737958331952853208805511
#             12540698747158523863050715693290963295227443043557
#             66896648950445244523161731856403098711121722383113
#             62229893423380308135336276614282806444486645238749
#             30358907296290491560440772390713810515859307960866
#             70172427121883998797908792274921901699720888093776
#             65727333001053367881220235421809751254540594752243
#             52584907711670556013604839586446706324415722155397
#             53697817977846174064955149290862569321978468622482
#             83972241375657056057490261407972968652414535100474
#             82166370484403199890008895243450658541227588666881
#             16427171479924442928230863465674813919123162824586
#             17866458359124566529476545682848912883142607690042
#             24219022671055626321111109370544217506941658960408
#             07198403850962455444362981230987879927244284909188
#             84580156166097919133875499200524063689912560717606
#             05886116467109405077541002256983155200055935729725
#             71636269561882670428252483600823257530420752963450"""

# start_time = perf_counter()
# print(find_greatest_product(number_str, k))
# end_time = perf_counter()
# print(end_time - start_time)

# optimal approach
def find_max_product(number, sequence_length):
    max_product = 0
    current_product = 1
    zero_count = 0

    for i in range(sequence_length):
        if number[i] == '0':
            zero_count += 1
        else:
            current_product *= int(number[i])

    if zero_count == 0:
        max_product = current_product

    for i in range(sequence_length, len(number)):
        exit_digit = int(number[i - sequence_length])
        enter_digit = int(number[i])

        if exit_digit == 0:
            zero_count -= 1
        else:
            current_product //= exit_digit

        if enter_digit == 0:
            zero_count += 1
        else:
            current_product *= enter_digit

        if zero_count == 0 and current_product > max_product:
            max_product = current_product

        if exit_digit == 0:
            current_product = 1
            zero_count = 0
            for j in range(i - sequence_length + 1, i + 1):
                if number[j] == '0':
                    zero_count += 1
                else:
                    current_product *= int(number[j])
            if zero_count == 0:
                max_product = max(max_product, current_product)

    return max_product
