def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def euler_009():
    val = 1000
    for a in range(1, val // 3):
        for b in range(a + 1, (val - a) // 2):
            c = 1000 - a - b
            if is_pythagorean_triplet(a, b, c):
                print(a, b, c, a * b * c)

if __name__ == '__main__':
    euler_009()