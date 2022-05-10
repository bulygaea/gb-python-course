with open("task3.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(*[i.split()[0] for i in lines if float(i.split()[1]) < 20000])
    print(sum([float(i.split()[1]) for i in lines]) / len(lines))
