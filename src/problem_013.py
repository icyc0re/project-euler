import os

def load_input(filename):
    with open(filename) as fr:
        return [int(line.strip()) for line in fr.readlines()]

def easy_013(numbers):
    return str(sum(numbers))[:10]

def add_digitlist(n1, n2):
    get_value = lambda vals, idx: vals[idx] if len(vals) > idx else 0

    res = []
    carry = 0
    for i in range(max(len(n1), len(n2))):
        d = get_value(n1, i) + get_value(n2, i) + carry
        res.append(d % 10)
        carry = d // 10
    if carry > 0:
        res.append(carry)
    return res

def euler_013(numbers):
    # treat each number as a list of digits and handle the sum
    # to simplify, reverse the order too
    numbers = [[int(c) for c in reversed(str(n))] for n in numbers]
    # add all numbers, digit by digit
    current_sum = numbers[0]
    for n in numbers[1:]:
        current_sum = add_digitlist(current_sum, n)
    
    return ''.join(map(str, current_sum[-10:][::-1]))

if __name__ == '__main__':
    input_filename = os.path.join(os.path.dirname(__file__), 'input/problem_013.txt')
    input_value = load_input(input_filename)
    print(easy_013(input_value))
    print(euler_013(input_value))
