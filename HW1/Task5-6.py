revenue = int(input("Type the company's revenue: "))
costs = int(input("Type the company's costs: "))
print(f"The company's financial result is {'profit' if revenue > costs else 'a loss'}")

if revenue > costs:
    print(f"Profitability of revenue: {(revenue - costs) / revenue}")
    number_of_employees = int(input("Type the number of employees: "))
    print(f"Profit per employee: {(revenue - costs) / number_of_employees}")
