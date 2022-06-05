class Matrix:
    def __init__(self, m):
        self.__matrix = m

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.__matrix])

    def __iter__(self):
        return (element for element in self.__matrix)

    def __add__(self, other):
        return Matrix([[j1 + j2 for j1, j2 in zip(i1, i2)] for i1, i2 in zip(self.__matrix, other)])


matrix1 = Matrix([[31, 32],
                  [37, 43],
                  [51, 86]])
matrix2 = Matrix([[-31, 0],
                  [-27, 17],
                  [19, -16]])

print(matrix1)
print('-----------')
print(matrix2)
print('-----------')
print(matrix1 + matrix2)
