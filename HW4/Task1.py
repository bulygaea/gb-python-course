from sys import argv


def salary_counter(production, rate, prize):
    return (production * rate) + prize


print(salary_counter(int(argv[1]), int(argv[2]), int(argv[3])))
