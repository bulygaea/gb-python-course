def my_func(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


print(my_func(int(input()), int(input()), int(input())))
