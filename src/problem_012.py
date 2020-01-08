from itertools import count
import math

def generate_triangle_numbers():
    partialsum = 0
    for n in count(1):
        partialsum += n
        yield partialsum

def count_factors(n):
    if n < 2: return n
    divisors = 1
    root = math.sqrt(n)
    for f in range(2, int(root)):
        if n % f == 0:
            divisors += 1
    if root.is_integer():
        return divisors * 2 + 1
    return divisors * 2

def euler_012(n):
    triangle_nums = generate_triangle_numbers()
    for _ in count():
        v = next(triangle_nums)
        factors = count_factors(v)
        if factors > n:
            return v

if __name__ == '__main__':
    print(euler_012(5))
    print(euler_012(500))
