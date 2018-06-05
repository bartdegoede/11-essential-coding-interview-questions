
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for bomb in bombs:
        row_i = bomb[0]
        col_i = bomb[1]
        field[row_i][col_i] = -1
        for i in range(row_i - 1, row_i + 2):
            for j in range(col_i - 1, col_i + 2):
                if 0 <= i < num_rows and 0 <= j < num_cols:
                    if field[i][j] != -1:
                        field[i][j] += 1

    return field


def click(field, num_rows, num_cols, x, y):
    if field[x][y] != 0:
        return field
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        field[x][y] = -2
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] == 0:
                    stack.append((i, j))

    return field





# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


if __name__ == '__main__':
    assert(mine_sweeper([[0, 2], [2, 0]], 3, 3) == [[0, 1, -1], [1, 2, 1], [-1, 1, 0]])
    assert(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) == [[-1, -1, 2, 1], [2, 3, -1, 1], [0, 1, 1, 1]])
    assert(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) == [[1, 2, 2, 1, 0], [1, -1, -1, 2, 0], [1, 3, -1, 2, 0], [0, 1, 2, 2, 1], [0, 0, 1, -1, 1]])

    field1 = [[0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 1, -1, 1, 0]]
    assert(click(field1, 3, 5, 2, 2) == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, -1, 1, 0]])

    assert(click(field1, 3, 5, 1, 4) == [[-2, -2, -2, -2, -2], [-2, 1, 1, 1, -2], [-2, 1, -1, 1, -2]])

    field2 = [[-1, 1, 0, 0],
              [1, 1, 0, 0],
              [0, 0, 1, 1],
              [0, 0, 1, -1]]
    assert(click(field2, 4, 4, 0, 1) == [[-1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]])
