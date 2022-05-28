from random import randint

with open("task5.txt", 'w', encoding="utf-8") as f:
    print(*[randint(-100, 100) for i in range(10)], file=f)

with open("task5.txt", 'r', encoding="utf-8") as f:
    print(sum(list(map(int, f.readline().split()))))
