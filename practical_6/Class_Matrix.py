class Matrix:
    def __init__(self, *args, **kwargs):
        """
        kwargs['filename']
        kwargs['list']
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self._read_as_list(kwargs['list'])


def read_as_list(self, matrix_list):
    self._matrix = ...
    self._columns = ...
    self._rows = ...


def read_from_file(self, filename):
    matrix_list = ...  # Read from file and store the list
    self.read_as_list(matrix_list)


def write_to_file(self, filename):
    pass


def transpose(self):
    pass


def shape(self):
    return self._columns, self._rows


def __add__(self, other):  # +
    pass


def __mul__(self, other):  # *
    pass


def __matmul__(self, other):  # @
    pass


matrix_1 = Matrix(filename='A.txt')
matrix_2 = Matrix(filename='B.txt')
print(matrix_1 @ matrix_2)  # matrix_1.__matmul__(matrix_2)
