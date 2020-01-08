import re
import os
from functools import reduce
import operator

def load_input(filename):
    with open(filename) as fr:
        return re.sub(r'[\D]', '', fr.read())

def highest_adjacent_product(digit_list, length):
    highest = -1
    for i in range(len(digit_list) - length):
        product = reduce(operator.mul, digit_list[i : i+length])
        if product > highest:
            highest = product
    return highest

# take n as a string
def euler_008(n: str):
    digits = [int(c) for c in n]
    return highest_adjacent_product(digits, 13)

if __name__ == '__main__':
    input_filename = os.path.join(os.path.dirname(__file__), 'input/problem8.txt')
    input_value = load_input(input_filename)
    print(euler_008(input_value))