# brute-force approach

def find_pythagorean_triplet(sum_of_triplet: int) -> int:
    for a in range(1, sum_of_triplet // 3):
        for b in range(a, sum_of_triplet // 2):
            c = sum_of_triplet - a - b
            if a * a + b * b == c * c:
                return [a, b, c]
    return None

def product_of_triplet(triplet):
    if triplet:
        return triplet[0] * triplet[1] * triplet[2]
    return None

triplet = find_pythagorean_triplet(10000)
product = product_of_triplet(triplet)

if triplet:
    print(f"The Pythagorean triplet is {triplet} and its product is {product}.")
else:
    print("No Pythagorean triplet found.")


