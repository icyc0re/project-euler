def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def euler_009():
    n_sum = 1000
    for a in range(1, n_sum // 3):
        for b in range(a + 1, (n_sum - a) // 2):
            c = n_sum - a - b
            if is_pythagorean_triplet(a, b, c):
                print(a, b, c, a * b * c)

if __name__ == '__main__':
    euler_009()