import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for v in range(2, int(math.sqrt(n)) + 1):
        if n % v == 0: return False
    return True

def primes():
    # generator
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2

def euler_007(n):
    p = primes()
    for _ in range(n-1):
        next(p)
    return next(p)

if __name__ == '__main__':
    print(euler_007(10001))
