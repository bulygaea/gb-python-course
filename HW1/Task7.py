a = int(input())
b = int(input())
day = 0

while a < b:
    day += 1
    print(f"{day}-й день: {a:3.2f}")
    a *= 1.1

print(f"На {day}-й день спортсмен достиг результата - не менее {b} км.")
