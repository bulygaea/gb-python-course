"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""


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
