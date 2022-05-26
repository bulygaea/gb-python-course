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
