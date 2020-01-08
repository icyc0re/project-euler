# Analytical solution (runs in O(1))

def sum_of_range(n):
    return (n + 1) * n // 2

def sum_of_multiples(n, high_bound):
    return sum_of_range((high_bound - 1) // n) * n

def multiples_3_5(high_bound):
    mul_3 = sum_of_multiples(3, high_bound)
    mul_5 = sum_of_multiples(5, high_bound)
    mul_15 = sum_of_multiples(15, high_bound)
    return mul_3 + mul_5 - mul_15

if __name__ == '__main__':
    result = multiples_3_5(1000)
    print(result)
