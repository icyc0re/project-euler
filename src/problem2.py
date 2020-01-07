import itertools

def generate_fibo():
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b

def main():
    is_even = lambda x: x % 2 == 0
    upperbound_4m = lambda x: x < 4000000
    even_fibo = filter(is_even, generate_fibo())
    valid_values = itertools.takewhile(upperbound_4m, even_fibo)
    result = sum(valid_values)
    print(f'Sum to 4 millions: {result}')

if __name__ == '__main__':
    main()