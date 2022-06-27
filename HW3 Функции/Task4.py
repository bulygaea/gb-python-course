"""4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение
числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без
встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя способами. Первый —
возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая
использование цикла. """


def my_func(x, y):
    r"""
    :param x: a positive float number
    :type x: float

    :param y: a negative integer
    :type y: int

    :return: the value of the degree of x in y
    :rtype: float
    """
    return 1 / my_func(x, -y) if y < 0 else 1 if y == 0 else x * my_func(x, y - 1)


print(my_func(float(input()), int(input())))
