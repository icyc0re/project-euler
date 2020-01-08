# No need to check for primes, non-primes are already multiples of smaller values
def euler_003(value):
    n = 2
    while value > 1:
        if value % n == 0:
            value //= n
        else:
            n += 1
    return n

if __name__ == '__main__':
    result = euler_003(600851475143)
    print('Highest factor: {}'.format(result))