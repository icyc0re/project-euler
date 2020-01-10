import itertools

def generate_fibo():
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b

def euler_002():
    even_fibo = filter(lambda x: x % 2 == 0, generate_fibo())
    bounded_values = itertools.takewhile(lambda x: x < 4000000, even_fibo)
    return sum(bounded_values)

def main():
    print(f'Sum to 4 millions: {euler_002()}')

if __name__ == '__main__':
    main()