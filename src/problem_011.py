import os
import operator
from functools import reduce

def load_input(filename):
    with open(filename) as fr:
        content = [list(map(int, line.strip().split(' '))) for line in fr.readlines()]
    return content

def compute_highest(values, k):
    return max([reduce(operator.mul, line[i:i+k]) for line in values
        for i in range(len(line) - k)])

# expects NxN matrix
def euler_011(values):
    k = 4
    size = len(values)

    # compute highest horizontal
    h1 = compute_highest(values, k)
    
    # compute highest vertical
    values2 = [[val[row] for val in values] for row, _ in enumerate(values)]
    h2 = compute_highest(values2, k)

    # compute highest diagonal (top left - bottom-right)
    values3 = [[1] * size for _ in range(size*2)]
    for r, row in enumerate(values):
        for c, n in enumerate(row):
            values3[size-r+c][r] = n
    h3 = compute_highest(values3, k)

    # compute highest diagonal (top right - bottom left)
    values4 = [[1] * size for _ in range(size*2)]
    for r, row in enumerate(values):
        for c, n in enumerate(row):
            values4[r+c][r] = n
    h4 = compute_highest(values4, k)

    return max([h1, h2, h3, h4])

if __name__ == '__main__':
    input_filename = os.path.join(os.path.dirname(__file__), 'input/problem_011.txt')
    input_value = load_input(input_filename)
    print(euler_011(input_value))
