import copy


def rotate_copy(given_array, n):
    new_array = copy.deepcopy(given_array)
    for row in range(n):
        for column in range(n):
            new_array[row][n - 1 - column] = given_array[column][row]

    return new_array


def rotate(given_array, n):
    stack = []
    for row in range(n):
        for column in range(n):
            stack.append((row, n - 1 - column, given_array[column][row]))
    while stack:
        x, y, value = stack.pop()
        given_array[x][y] = value
    return given_array


if __name__ == '__main__':
    a1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    assert(rotate_copy(a1, 3) == [[7, 4, 1],
                                  [8, 5, 2],
                                  [9, 6, 3]])
    assert(rotate(a1, 3) == [[7, 4, 1],
                             [8, 5, 2],
                             [9, 6, 3]])
    a2 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
    assert(rotate_copy(a2, 4) == [[13, 9, 5, 1],
                                  [14, 10, 6, 2],
                                  [15, 11, 7, 3],
                                  [16, 12, 8, 4]])
    assert(rotate(a2, 4) == [[13, 9, 5, 1],
                             [14, 10, 6, 2],
                             [15, 11, 7, 3],
                             [16, 12, 8, 4]])
