n = int(input("How much elements do you want to add? "))
a = [int(input("Type the result: ")) for i in range(n)]
for i in range(1, n, 2):
    a[i-1], a[i] = a[i], a[i-1]
print(*a)
