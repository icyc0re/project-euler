import os

def load_input(filename):
    with open(filename) as fr:
        return fr.read().strip().replace('"', '').split(',')

def euler_022(namelist):
    ord_a = ord('A')
    letter_value = lambda c: ord(c) - ord_a + 1
    name_value = lambda name: sum(map(letter_value, name))

    # sort list
    namelist = sorted(namelist)

    # compute scoring
    namescores = map(name_value, namelist)
    scores = map(lambda v: v[0] * v[1], enumerate(namescores, 1))
    return sum(scores)

if __name__ == '__main__':
    input_filename = os.path.join(os.path.dirname(__file__), 'input/problem_022.txt')
    input_value = load_input(input_filename)
    print(euler_022(input_value))
