import math

def euler_003(value):
    # generate primes until 1000000
    primes = [False, False, True] + [True] * 999998
    for n, is_prime in enumerate(primes):
        if is_prime:
            if value % n == 0:
                value //= n
                if value == 1:
                    return n
            for k in range(n * 2, len(primes), n):
                primes[k] = False

if __name__ == '__main__':
    print('Highest factor: {}'.format(euler_003(600851475143)))