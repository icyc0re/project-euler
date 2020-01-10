# in a NxN grid we have to travel
# N horizontal segments and N vertical segments
# the number of paths is all the possible orders of such elements
#
# we have 2 groups of elements (horizontal, vertical)
# we calculate all possible combinations: factorial(horizontal+vertical)
# then we divide it by the permutations (all possible ordering) of horizontal
# and same for vertical
#
# final formula: factorial(N + N) / factorial(N) / factorial(N)

from math import factorial

def euler_015(grid_size):
    return factorial(grid_size * 2) // factorial(grid_size) ** 2

if __name__ == '__main__':
    # print(euler_015(2))
    print(euler_015(20))
