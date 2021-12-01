def convolution(matrix_a, matrix_b):
    r, c = len(matrix_a), len(matrix_a[0])

    new_r, new_c = r - len(matrix_b) + 1, c - len(matrix_b[0]) + 1
    result_matrix = [[0] * new_c for _ in range(new_r)]

    for row in range(new_r):
        for col in range(new_c):
            spider_ls = get_spider_from_matrix(
                matrix_a=matrix_a, matrix_b=matrix_b,
                row_start_idx=row, col_start_idx=col
            )

            result_matrix[row][col] = matmul(matrix_a=spider_ls, matrix_b=matrix_b)

    return result_matrix


def get_spider_from_matrix(matrix_a, matrix_b, row_start_idx, col_start_idx):
    spider_len = len(matrix_b)

    spider_ls = []
    for idx_row_spdr in range(spider_len):
        spider_ls.append(matrix_a[row_start_idx + idx_row_spdr][col_start_idx:col_start_idx + 3])
    return spider_ls


def matmul(matrix_a, matrix_b):
    """
    Mathematical matrix multiplication.
    :param matrix_a:
    :param matrix_b:
    :return:
    """

    r = len(matrix_a)
    c = len(matrix_a[0])

    summary = 0
    # iterate through rows
    for i in range(r):
        # iterate through columns
        for j in range(c):
            summary += matrix_a[i][j] * matrix_b[i][j]

    return summary


matrix_I = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0]
]

matrix_K = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(convolution(matrix_I, matrix_K))
