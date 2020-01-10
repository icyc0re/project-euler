def euler_010(upper_bound):
    sieve = [False, False, True] + [True] * (upper_bound - 3)
    partial_sum = 0
    for n, p in enumerate(sieve):
        if p:
            partial_sum += n
            for k in range(n * 2, upper_bound, n):
                sieve[k] = False
    return partial_sum

if __name__ == '__main__':
    # print(euler_010(10))
    print(euler_010(2000000))
            