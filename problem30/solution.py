def sum_of_digit_powers(n: int) -> int:
    limit = 6 * 9**n
    total_sum = 0

    for number in range (2, limit):
            sum_of_power = sum(int(digit)**n for digit in str(number))
            if sum_of_power == number:
                total_sum += number
    return total_sum
print(sum_of_digit_powers(5))