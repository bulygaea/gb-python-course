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
