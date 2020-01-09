import os

def load_input(filename):
    with open(filename) as fr:
        return [[int(n) for n in line.strip().split(' ')] for line in fr.readlines()]

def euler_018(values):
    for prev, line in zip(values[:-1], values[1:]):
        line[0] += prev[0]
        line[-1] += prev[-1]
        for i, _ in enumerate(line[1:-1]):
            line[i+1] += max(prev[i:i+2])
    return max(values[-1])

if __name__ == '__main__':
    input_filename = os.path.join(os.path.dirname(__file__), 'input/problem_018.txt')
    input_value = load_input(input_filename)
    print(euler_018(input_value))
