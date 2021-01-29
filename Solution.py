from time import time


def get_triangle_file(triangle_file):
    triangle = [[int(i) for i in row.split()] for row in open(triangle_file)]
    return triangle


def maximal_total(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            maximum = max(triangle[i][j], triangle[i][j + 1])
            triangle[i - 1][j] += maximum
    return triangle[0][0]


if __name__ == '__main__':
    start_time = time()
    tri = get_triangle_file('triangle.txt')
    print(f'Maximum Total:{maximal_total(tri)}')
    print(f'Execution Time: {time() - start_time} seconds.')
