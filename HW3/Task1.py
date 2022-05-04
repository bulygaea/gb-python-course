def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        return err


print(divider(int(input()), int(input())))
