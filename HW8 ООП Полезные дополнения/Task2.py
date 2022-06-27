"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой. """


class MyZeroDivisionError(ZeroDivisionError):
    def __str__(self):
        return 'Attention! Don\'t divide by zero!'


a = float(input('Type the divisible: '))
b = float(input('Type the divisor: '))
try:
    if b == 0:
        raise MyZeroDivisionError()
    print(a / b)
except MyZeroDivisionError as err:
    print(err)
