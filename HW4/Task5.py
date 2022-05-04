from functools import reduce

even_nums = [i for i in range(100, 1001, 2)]
print(reduce(lambda prev, el: prev * el, even_nums))
