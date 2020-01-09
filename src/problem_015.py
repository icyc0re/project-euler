# each cell can only be reached by left and top
#
# this means that the # of paths that reach a cell is
# the sum of the # of paths that reach the left cell and the top cell
# the first line has only one path
# the second line has 1,2,3,4,... paths
# ...
# we can iteratively calculate each line, by summing values

def euler_015(grid_size):
    paths = list(range(1, grid_size + 2))
    for _ in range(1, grid_size):
        for i in range(1, grid_size + 1):
            paths[i] += paths[i - 1]
    return paths[-1]

if __name__ == '__main__':
    # print(euler_015(2))
    print(euler_015(20))
