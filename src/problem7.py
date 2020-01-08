def compute_primes(upper_bound):
    is_prime = [False, False, True] + [True] * (upper_bound - 3)
    for n, p in enumerate(is_prime):
        if p:
            for k in range(n * 2, upper_bound, n):
                is_prime[k] = False
    return is_prime

def euler_007(n):
    UPPER_BOUND = 200000
    primes = compute_primes(UPPER_BOUND)
    cnt = 0
    for v, p in enumerate(primes):
        if p:
            cnt += 1
        if cnt == n:
            return v
    raise Exception('UPPER BOUND REACHER, increase to find more primes')
    
if __name__ == '__main__':
    # print(euler_007(6))
    print(euler_007(10001))
