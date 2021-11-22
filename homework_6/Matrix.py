from csv import writer


class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

        self._matrix = []
        self._columns = 0
        self._rows = 0

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return self._matrix

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0
        #print('Successfully raed from the list')

    def read_from_file(self, filename):
        file_full_name = f'{filename}.csv'
        with open(file_full_name, 'r') as f:
            matrix_list = f.readlines()
        print('matrix_list\n', matrix_list)
        matrix_list = list(
            map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)
        #print('Successfully read from the file.')

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        file_full_name = f'{filename}.csv'
        data = self._matrix
        with open(file_full_name, 'a+') as f_object:
            writer_object = writer(
                f_object, delimiter=' ', lineterminator='\n'
            )
            for ls in data:
                writer_object.writerow(ls)
        print(f'Data has been written to the file {file_full_name}')

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def transpose(self, save=False):
        """
        Transpose the matrix.
        TODO: implement
        """
        matrix = self._matrix
        flattened_matrix = list(zip(*matrix))
        transposed_matrix = [[*elem] for elem in flattened_matrix]
        if save:
            self._matrix = transposed_matrix
            self._columns, self._rows = self._rows, self._columns
            return self

        new_transposed_matrix = Matrix()
        new_transposed_matrix.read_as_list(transposed_matrix)
        return new_transposed_matrix

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        if not isinstance(other, Matrix):
            raise AttributeError(f'Data types must be list')

        if self.shape != other.shape:
            raise AttributeError(
                f"Shapes mismatching {self.shape} and {other.shape}"
            )

        result = [[0] * self._columns for _ in range(self._rows)]

        # iterate through rows
        for i in range(self._rows):
            # iterate through columns
            for j in range(self._columns):
                result[i][j] = self._matrix[i][j] + other._matrix[i][j]

        c = Matrix()
        c.read_as_list(matrix_list=result)
        return c

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise AttributeError(f'Data types must be list')

        if self.shape != other.shape:
            raise AttributeError(
                f"Shapes mismatching {self.shape} and {other.shape}"
            )

        result = [[0] * self._columns for _ in range(self._rows)]

        # iterate through rows
        for i in range(self._rows):
            # iterate through columns
            for j in range(self._columns):
                result[i][j] = self._matrix[i][j] - other._matrix[i][j]

        c = Matrix()
        c.read_as_list(matrix_list=result)
        return c

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        if not isinstance(other, (Matrix, int, float)):
            raise AttributeError(
                f'Attribute must be of class Matrix, int or float')

        result = []
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise AttributeError(
                    f"Shapes mismatching {self.shape} and {other.shape}"
                )
            result = [[0] * self._columns for _ in range(self._rows)]

            # iterate through rows
            for i in range(self._rows):
                # iterate through columns
                for j in range(self._columns):
                    result[i][j] = self._matrix[i][j] * other._matrix[i][j]

        elif isinstance(other, (int, float)):
            result = []
            for i in range(self._rows):
                result.append([])
                for j in range(self._columns):
                    result[i].append(other * self._matrix[i][j])

        c = Matrix()
        c.read_as_list(matrix_list=result)
        return c

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number
        of rows in the second matrix.
        TODO: implement
        """
        if self._columns != other._rows:
            raise AssertionError(
                f'The number of columns in the first matrix must be equal to'
                f' the number of rows in the second matrix : First matrix ->'
                f' ({self.shape}),Second matrix -> ({other.shape})'
            )
        else:
            transposed_matrix_obj = other.transpose(save=False)
            transposed_matrix = transposed_matrix_obj._matrix
            return [
                [sum(elem_slf_m * elem_tr_m
                     for elem_slf_m, elem_tr_m in zip(row_slf_m, col_tr_m)
                     ) for col_tr_m in transposed_matrix
                 ]
                for row_slf_m in self._matrix
            ]

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        if self._columns != self._rows:
            raise NotImplemented(
                "For non square matrices trace is not defined."
            )
        tr = 0
        for i in range(self._columns):
            tr += self._matrix[i][i]
        return tr

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        if self._columns != self._rows:
            raise ValueError("Not square matrix!")
        if self._columns == 1:
            return self._matrix[0][0]

        matrix = self._matrix
        det = Matrix.get_determinant(matrix)
        return det

    @staticmethod
    def minor(a_matrix, i, j):
        matrix = a_matrix[:i] + a_matrix[i + 1:]
        for k in range(0, len(matrix)):
            matrix[k] = matrix[k][:j] + matrix[k][j + 1:]
        return matrix

    @staticmethod
    def get_determinant(array):
        n = len(array)
        if n == 1:
            return array[0][0]
        if n == 2:
            return array[0][0] * array[1][1] - array[0][1] * array[1][0]
        summ = 0
        for i in range(0, n):
            m = Matrix.minor(array, 0, i)
            summ = summ + ((-1) ** i) * array[0][i] * Matrix.get_determinant(m)
        return summ


# Testing
if __name__ == '__main__':
    m1 = Matrix()
    m1.read_as_list([[1, 2, 3],
                     [4, 5, 6],
                     [7, 7, 9]])
    print(m1)
    print('Shape ->', m1.shape)
    print('Determinant ->', m1.determinant)

    print('/' * 50)
    m2 = Matrix()
    m2.read_as_list([[10, 11],
                     [20, 21],
                     [30, 31]])
    print(m2)

    print('/' * 50)
    # Element-wise matrix multiplication
    print('Matrix Element-wise multiplication by int \n', m1 * 5)
    print('Matrix Element-wise multiplication by Matrix \n', m1 * m1)

    print('/' * 50)
    print('Mathematical matrix multiplication.')
    m3 = m1 @ m2
    print(m3)

    print('/' * 50)
    print('Matrix transposition')
    print(m1.transpose(save=False))
    print(m1)

    print('/' * 50)
    print('Before \n', m2)
    print(m2.transpose(save=True))
    print('After \n', m2)

    print('/' * 50)
    print('Trace ->', m1.trace)

    print('/' * 50)
    print("m1 + m1", m1 + m1)
    print("m1 - m1", m1 - m1)

    print('/' * 50)
    print('Write matrix to csv file.')
    m1.write_to_file(filename='matrix_1')

    print('/'*50)
    print('Loading matrix from csv file.')
    m3 = Matrix()
    m3.read_from_file(filename='matrix_1')
    print(m3)
