"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль. """


def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        return err


print(divider(int(input()), int(input())))
