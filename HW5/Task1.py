with open("task1.txt", 'w') as f:
    while True:
        line = input('Type the line: ')
        if not line:
            break
        f.write(f"{line}\n")
