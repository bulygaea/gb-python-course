"""5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
сообщение.
6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника. """

revenue = int(input("Type the company's revenue: "))
costs = int(input("Type the company's costs: "))
print(f"The company's financial result is {'profit' if revenue > costs else 'a loss'}")

if revenue > costs:
    print(f"Profitability of revenue: {(revenue - costs) / revenue}")
    number_of_employees = int(input("Type the number of employees: "))
    print(f"Profit per employee: {(revenue - costs) / number_of_employees}")
