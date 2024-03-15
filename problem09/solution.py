for a in range(1, 333):
    for b in range(a + 1, 500):  # b is more than a and less than 500 since a+b+c=1000 and a<b<c
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a, b, c) 
            print(a*b*c)
            break  # once the correct triplet is found, we don't need to search further
    else:
        continue
    break  # break the outer loop if the triplet is found
