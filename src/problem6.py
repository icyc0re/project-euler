def sum_of_squares(n):
    return sum([v * v for v in range(1, n + 1)])

def square_of_sum(n):
    return ((n + 1) * n // 2) ** 2

def euler_006(n):
    return square_of_sum(n) - sum_of_squares(n)

if __name__ == '__main__':
    # print(euler_006(10))
    print(euler_006(100))
