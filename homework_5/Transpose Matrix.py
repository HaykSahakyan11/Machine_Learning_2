# 867. Transpose Matrix

def transpose(a_matrix):
    transposed_matrix = list(zip(*a_matrix))
    if isinstance(my_matrix, list):
        transposed_matrix = [[*elem] for elem in transposed_matrix]
    return transposed_matrix


my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(my_matrix))
