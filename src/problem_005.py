# Analytical solution to a least common multiple problem:
# - find all prime factors for all values
# - get all factors with the highest exponent found

from functools import reduce
import operator

def get_prime_factors(value):
    factors = {}
    n = 2
    while value > 1:
        if value % n == 0:
            factors[n] = factors.get(n, 0) + 1
            value //= n
        else:
            n += 1
    return factors

def combine_dicts(factors1, factors2):
    for k, v in factors2.items():
        if factors1.get(k, 0) < v:
            factors1[k] = v

# accepts input n >= 2
def euler_005(n):
    factors = {}
    for v in range(2, n + 1):
        factors_v = get_prime_factors(v)
        combine_dicts(factors, factors_v)
    
    # compute result
    return reduce(operator.mul, [k ** v for k, v in factors.items()])

if __name__ == '__main__':
    print(euler_005(20))
