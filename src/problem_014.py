# improve solution with memoization

def next_value(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def compute_collatz_sequence(n, memo):
    cnt = 0
    while n not in memo.keys():
        cnt += 1
        n = next_value(n)
    return memo[n] + cnt

def euler_014(n):
    memo = {1: 1}
    for v in range(1, n):
        cnt = compute_collatz_sequence(v, memo)
        memo[v] = cnt
    return max(memo.items(), key=lambda x: x[1])

if __name__ == '__main__':
    print(euler_014(1000000))
