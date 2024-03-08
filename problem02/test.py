

def sum_even_fibo(numb: int) -> int:
    x0 = 1
    x1 = 1
    sum = 0
    x_prev = x0
    x_current = x1
    while x_current < numb:
        # update
        x_new = x_prev + x_current
        x_prev = x_current
        x_current = x_new
        if x_current % 2 == 0:
            sum += x_current
    return sum

if __name__ == "__main__":
    numb = 4000000
    print(f'The sum of even Fiboncci number less than {numb} is {sum_even_fibo(numb)}')

    