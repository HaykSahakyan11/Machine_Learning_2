# 48. Rotate Image

def rotate(matrix):
    matrix_copy = matrix.copy()
    matrix_copy.reverse()

    for i in range(len(matrix_copy)):
        for j in range(i):
            matrix_copy[i][j], matrix_copy[j][i] =\
                matrix_copy[j][i], matrix_copy[i][j]
    return matrix_copy


def pretty_print(ls):
    for row in ls:
        print(row)


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('Matrix Before')
pretty_print(matrix_1)
print('*' * 30)
print('Matrix After')
pretty_print(rotate(matrix=matrix_1))

